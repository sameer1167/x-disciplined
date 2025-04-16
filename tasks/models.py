import uuid
from django.db import models
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Users

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', _('New')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        COMPLETED = 'COMPLETED', _('Completed')
        OVERDUE = 'OVERDUE', _('Overdue')

    class RecurrenceFrequency(models.TextChoices):
        DAILY = 'DAILY', _('Daily')
        WEEKLY = 'WEEKLY', _('Weekly')
        MONTHLY = 'MONTHLY', _('Monthly')
        
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    email_alert = models.BooleanField(default=False)
    sound_alert = models.BooleanField(default=False)
    notification_alert = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    # Repeat feature fields
    is_recurring = models.BooleanField(default=False)
    recurrence_frequency = models.CharField(
        max_length=20,
        choices=RecurrenceFrequency.choices,
        blank=True,
    )
    recurrence_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    

    def calculate_next_occurrence(self):
        if not self.is_recurring or (self.recurrence_end_date and self.due_date.date() >= self.recurrence_end_date):
            return None

        if self.recurrence_frequency == self.RecurrenceFrequency.DAILY:
            return self.due_date + timezone.timedelta(days=1)
        elif self.recurrence_frequency == self.RecurrenceFrequency.WEEKLY:
            return self.due_date + timezone.timedelta(weeks=1)
        elif self.recurrence_frequency == self.RecurrenceFrequency.MONTHLY:
            return self.due_date + timezone.timedelta(weeks=4)  # Simplified for monthly, consider using a more accurate method
        return None

    def complete_task(self):
        # Mark this instance as completed for the day
        self.status = self.Status.COMPLETED
        next_due_date = self.calculate_next_occurrence()
        if next_due_date:
            Task.objects.create(
                user=self.user,
                title=self.title,
                due_date=next_due_date,
                is_recurring=self.is_recurring,
                recurrence_frequency=self.recurrence_frequency,
                recurrence_end_date=self.recurrence_end_date,
                status=self.Status.COMPLETED
            )
        self.save()
    

