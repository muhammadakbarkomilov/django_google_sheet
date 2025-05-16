from django.apps import AppConfig

class googlshConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'googlsh'

    def ready(self):
        import googlsh.signals