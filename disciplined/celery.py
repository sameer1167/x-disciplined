import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disciplined.settings')

app = Celery('disciplined')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



#auto alarm trigger redis command
#  celery -A disciplined worker --loglevel=info
# celery -A disciplined beat --loglevel=info