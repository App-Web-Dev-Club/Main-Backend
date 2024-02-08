# yourapp/management/commands/send_birthday_wishes.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Send birthday wishes to users with today\'s date of birth'

    def handle(self, *args, **options):
        # today = datetime.today().date()
        # birthdays_today = User.objects.filter(dob__month=today.month, dob__day=today.day)

        # for birthday_person in birthdays_today:
            subject = 'Happy Birthday!'
            message = f"Dear\n\nHappy Birthday!\n\nBest wishes from us!"
            from_email = 'biwinfelix@gmail.com'  # Update with your email
            to_email = ['bewinfelix25@gmail.com']

            send_mail(subject, message, from_email, to_email)
            self.stdout.write(self.style.SUCCESS(f"Sent birthday wishes to"))
