from django.apps import AppConfig


class ReviewappConfig(AppConfig):
    name = 'reviewApp'
 
def ready(self):
	import users.signals

