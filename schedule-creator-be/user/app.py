import typing
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import router
import config
from config import CONFIG


# if not local environment hide api docs url
if CONFIG.env != 'local':
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()

app.include_router(router.router)

userDB = {'users': []}
