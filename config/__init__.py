import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import sentry_sdk
from mangum import Mangum

from config import urls


app = FastAPI(
    title="Photogram Backend",
    description="",
    version="v1",
)


handler = Mangum(app)


sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

origins = os.environ.get("ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    urls.urls
)
