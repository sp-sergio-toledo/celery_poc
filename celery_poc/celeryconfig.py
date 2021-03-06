from datetime import timedelta

BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_INCLUDE = ['celery_poc.tasks']

CELERYBEAT_SCHEDULE = {
    'schedule_add': {
        'task': 'add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16),
    },
}
