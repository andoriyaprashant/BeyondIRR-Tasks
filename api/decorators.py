import json
import logging
from functools import wraps
from django.http import JsonResponse
from .models import LogRequest
from datetime import datetime

logger = logging.getLogger('api')

def mask_sensitive_data(data, sensitive_keys=None):
    if sensitive_keys is None:
        sensitive_keys = ["password", "token", "secret"]

    if isinstance(data, dict):
        for key, value in data.items():
            if key.lower() in sensitive_keys:
                data[key] = "*****"
            elif isinstance(value, (dict, list)):
                data[key] = mask_sensitive_data(value, sensitive_keys)
    elif isinstance(data, list):
        data = [mask_sensitive_data(item, sensitive_keys) for item in data]

    return data

def log_request(record_success=False):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            logger.debug("Request logging started.")
            try:
                payload = json.loads(request.body.decode('utf-8')) if request.body else {}
                masked_payload = mask_sensitive_data(payload)
                logger.debug(f"Masked Payload: {masked_payload}")

                response = view_func(request, *args, **kwargs)
                logger.debug(f"Response: {response}")

                masked_response = mask_sensitive_data(response.data if isinstance(response, JsonResponse) else response)
                logger.debug(f"Masked Response: {masked_response}")

                if record_success or response.status_code >= 400:
                    LogRequest.objects.create(
                        url=request.path,
                        status_code=response.status_code,
                        method=request.method,
                        timestamp=datetime.now(),
                        payload=json.dumps(masked_payload),
                        response=json.dumps(masked_response),
                        is_success=response.status_code < 400
                    )
                    logger.info("Log entry created.")

                return response

            except Exception as e:
                logger.error("Exception occurred.", exc_info=True)
                LogRequest.objects.create(
                    url=request.path,
                    status_code=500,
                    method=request.method,
                    timestamp=datetime.now(),
                    payload=json.dumps(mask_sensitive_data(payload)),
                    response=json.dumps({"error": str(e)}),
                    is_success=False
                )
                return JsonResponse({"error": "An unexpected error occurred."}, status=500)

        return _wrapped_view
    return decorator

