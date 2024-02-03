# yourapp/management/commands/send_birthday_wishes.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from datetime import datetime
import schedule
import time

User = get_user_model()

class Command(BaseCommand):
    help = 'Send birthday wishes to users with today\'s date of birth'

    def send_birthday_wishes(self):
        today = datetime.today().date()
        birthdays_today = User.objects.filter(dob__month=today.month, dob__day=today.day)

        for birthday_person in birthdays_today:
            subject = 'Happy Birthday!'
            message = f"Dear {birthday_person.name},\n\nHappy Birthday!\n\nBest wishes from us!"
            from_email = 'your@example.com'  # Update with your email
            to_email = [birthday_person.email]

            send_mail(subject, message, from_email, to_email)
            self.stdout.write(self.style.SUCCESS(f"Sent birthday wishes to {birthday_person.name}"))

    def handle(self, *args, **options):
        # Schedule the job to run every day at 6 AM
        print('started')
        schedule.every().day.at("06:00").do(self.send_birthday_wishes)

        # Run the scheduler loop
        while True:
            schedule.run_pending()
            time.sleep(1)
