from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # def ready(self):
    #     # Run the custom command when the app is ready
    #     from django.core.management import call_command
    #     call_command('sendmail')
