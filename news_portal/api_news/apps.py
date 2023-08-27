from django.apps import AppConfig


class ApiNewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api_news"

    def ready(self):
        import api_news.signals