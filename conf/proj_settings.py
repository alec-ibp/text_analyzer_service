from __future__ import annotations

import os
from distutils.util import strtobool

from dotenv import load_dotenv


load_dotenv()


VERSION: str = "0.1.0"

INSTALLED_APPS: list[str] = [
    "posts",
]

DEBUG: bool = bool(strtobool(os.environ.get("DEBUG", "False")))
LOGGING: dict[str, str] = {}

BROKER_URL = os.environ.get("BROKER_URL")
POST_TOPIC: str = "posts"

# rds Database
RDS_HOSTNAME: str = os.environ.get("RDS_HOSTNAME", "localhost")
RDS_DB_NAME: str = os.environ.get("RDS_DB_NAME", "postgres")
RDS_USERNAME: str = os.environ.get("RDS_USERNAME", "postgres")
RDS_PASSWORD: str = os.environ.get("RDS_PASSWORD", "postgres")
RDS_PORT: str = os.environ.get("RDS_PORT", "5432")

# CORS
CORS_ALLOWED_METHODS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HEADERS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HOSTS: list[str] = os.environ.get("CORS_ALLOWED_HOSTS", "").split(",")
