from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta

# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-this")

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,0.0.0.0"
).split(",")

X_FRAME_OPTIONS = "ALLOWALL"


# =========================
# INSTALLED APPS
# =========================
INSTALLED_APPS = [

    # Admin Theme
    "jazzmin",

    # Django Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third Party
    "rest_framework",
    "corsheaders",

    # Local Apps
    "apps.core",
    "apps.programs",
    "apps.gallery",
    "apps.reports",
    "apps.members",
    "apps.health",
    "apps.environment",
    "apps.testimonials",
    "apps.contact",
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [

    # CorsMiddleware MUST be first
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    # CSRF — keep this if you use Django admin
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# CORS CONFIG
# =========================
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# =========================
# DJANGO REST FRAMEWORK
# =========================
REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}


# =========================
# JWT SETTINGS
# =========================
SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# =========================
# ROOT URL CONFIG
# =========================
ROOT_URLCONF = "srvngo.urls"


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================
# WSGI
# =========================
WSGI_APPLICATION = "srvngo.wsgi.application"


# =========================
# DATABASE (MYSQL)
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "srv_ngo"),
        "USER": os.getenv("DB_USER", "ngo_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "srv@123"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        },
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================
# LANGUAGE & TIMEZONE
# =========================
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ FIX: Only include if folder exists — prevents 400/500 on startup
STATICFILES_DIRS = [
    BASE_DIR / "static",
] if (BASE_DIR / "static").exists() else []


# =========================
# MEDIA FILES
# =========================
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================
# DEFAULT PRIMARY KEY
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================
# JAZZMIN ADMIN SETTINGS
# =========================
JAZZMIN_SETTINGS = {

    "site_title": "SRV NGO Admin",
    "site_header": "SRV NGO Dashboard",
    "site_brand": "SRV NGO",

    "site_logo": "images/logo.png",

    "welcome_sign": "Welcome to SRV NGO Management Panel",

    "copyright": "SRV NGO",

    "show_sidebar": True,
    "navigation_expanded": True,

    "topmenu_links": [
        {"name": "View Website", "url": "/", "new_window": True},
    ],

    "theme": "flatly",
    "dark_mode_theme": None,
    "custom_css": "css/admin_blue.css",

    "order_with_respect_to": [
        "core",
        "programs",
        "health",
        "environment",
        "gallery",
        "reports",
        "members",
        "testimonials",
        "contact",
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "core": "fas fa-building",
        "programs": "fas fa-tasks",
        "health": "fas fa-heartbeat",
        "environment": "fas fa-leaf",
        "gallery": "fas fa-images",
        "reports": "fas fa-file-alt",
        "members": "fas fa-user-friends",
        "testimonials": "fas fa-comment-dots",
        "contact": "fas fa-envelope",
    },

    "ui_tweaks": {
        "navbar_small_text": False,
        "footer_small_text": False,
        "body_small_text": False,
        "brand_small_text": False,
        "sidebar_small_text": False,
        "navbar_fixed": True,
        "sidebar_fixed": True,
        "footer_fixed": False,
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": True,
        "sidebar_nav_compact_style": False,
    },
}