from fastapi import Request
import http, time
from datetime import datetime
from configs.logger import logger

async def log_request_middleware(request: Request, call_next):
    """
    This middleware will log all requests and their processing time.
    E.g. log:
    0.0.0.0:1234 - GET /ping 200 OK 1.00ms
    """
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    
    formatted_process_time = "{0:.2f}".format(process_time)
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    try:
        status_phrase = http.HTTPStatus(response.status_code).phrase
    except ValueError:
        status_phrase = ""
    current_datetime = datetime.fromtimestamp(start_time).isoformat()
    # Log the request with date and time
    logger.info(f'{current_datetime} - {host}:{port} - "{request.method} {url}" {response.status_code} {status_phrase} {formatted_process_time} ms')

    return response