from celery import Celery

# Get the project settings module
project_settings = "web.settings"

# Create a new Celery app
app = Celery("web")

# Configure the Celery app using the project settings
app.config_from_object(project_settings, namespace="CELERY")

# Autodiscover tasks in the installed apps
app.autodiscover_tasks()
