from django.apps import AppConfig


class FridgeConfig(AppConfig):
    name = 'fridge'

    def ready(self):
        import fridge.signals