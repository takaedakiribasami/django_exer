from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガー設定
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    # ハンドラー設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },
    # フォーマッター設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
