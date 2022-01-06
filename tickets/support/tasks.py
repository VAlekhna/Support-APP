from tickets.celery import app
from celery import shared_task


@shared_task
def send_alert():
    print("Alert! New Question.")
    return "We have a new question."
