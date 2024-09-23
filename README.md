# Endpoint filter for the standard librarys logging module.
This package provides a filter for the standard librarys logging module 
that filters out log messages based on the request path of a FastAPI 
application.

## Usage

```python
from fastapi import FastAPI
import logging
from endpoint_filter import EndpointFilter

app = FastAPI()
uvicorn_logger = logging.getLogger("uvicorn.access")
uvicorn_logger.addFilter(EndpointFilter(path="/live"))
uvicorn_logger.addFilter(EndpointFilter(path="/endpoint"))



@app.get('/endpoint') # This endpoint will be ignored by the filter
async def endpoint():
    return {"message": "Hello endpoint"}

@app.get('/live') # This endpoint will be ignored by the filter
async def live():
    return {"message": "Hello live"}

@app.get('/')
async def root():
    return {"message": "Hello root"}
```
