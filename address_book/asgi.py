"""
ASGI config for address_book project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'address_book.settings')

application = get_asgi_application()



from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware
from django.core.wsgi import get_wsgi_application
from django.conf import settings



from apiApp.views import app_routes

def get_application() -> FastAPI:
    app = FastAPI(title='FastApi-Address-Book', debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(app_routes, prefix="/api")
    app.mount("/django", WSGIMiddleware(get_wsgi_application()))

    return app


app = get_application()