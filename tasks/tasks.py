# alarms/tasks.py
from celery import shared_task
from .models import Task
from users.models import Users
from django.utils import timezone
from django.core.mail import send_mail
# from tasks.utils import convert_user_time_to_utc, convert_utc_to_user_time

@shared_task
def check_alarms():
    now = timezone.now().replace(second=0, microsecond=0)
    alarms = Task.objects.filter(due_date=now)

    for alarm in alarms:
        if alarm.email_alert:
            send_mail(
                'Alarm Alert!',
                f"Hey {alarm.user.username}, you missed your goal '{alarm.title}'! Shame on you 😡!",
                'sheosam03@gmail.com',
                [alarm.user.email]
            )
        
        if alarm.sound_alert:
            print(f"[SOUND] Playing sound for alarm: {alarm.title}")

        if alarm.notification_alert:
            print(f"[NOTIFICATION] Sending system/push notification for {alarm.title}")
        
        
        alarm.save()
