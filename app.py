print('Starting Project: Chatbot Re-Ranking ::: ')
from fastapi import FastAPI, Request
import time, datetime, os
from configs.middleware import log_request_middleware
from configs.logger import configure_logging

from elasticapm import set_context
from starlette.requests import Request
from elasticapm.utils.disttracing import TraceParent
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv('configs/.env')

ALLOWED_ORIGINS = ['*']

app = FastAPI(
    title="Project Chat AI: Re Ranking API (2023)", 
    description=f"Created by music \n TNT Media and Network Co., Ltd. \n Started at {datetime.datetime.now().strftime('%c')}",
    docs_url="/",
    version="1.0.0",
    )

app.add_middleware(  
    CORSMiddleware,  
    allow_origins=ALLOWED_ORIGINS,  # Allows CORS for this specific origin  
    allow_credentials=True,  
    allow_methods=["*"],  # Allows all methods  
    allow_headers=["*"],  # Allows all headers  
)  

@app.middleware("http")  
async def add_process_time_header(request: Request, call_next):  
    trace_parent = TraceParent.from_headers(request.headers)  
    set_context({  
        "method": request.method,  
        "url_path": request.url.path,  
    }, 'request')  
    response = await call_next(request)  
    set_context({  
        "status_code": response.status_code,  
    }, 'response')  
    # Check if the status code is not in the range of 200-299  
    if 200 <= response.status_code < 300:  
        transaction_status = 'success'  
    else:  
        transaction_status = 'failure'  
    return response  

app.middleware("http")(log_request_middleware)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = "{0:.2f}ms".format(process_time)
    return response

if int(os.getenv("LOGGING")):
    configure_logging()

from routes.re_ranking_route import re_ranking_route
app.include_router(re_ranking_route)

print('Started Project: Chatbot Re-Ranking ::: ')