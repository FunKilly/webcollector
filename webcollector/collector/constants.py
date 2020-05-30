from django.db import models
from django.utils.translation import gettext_lazy as _


class ProcessingStatusType(models.TextChoices):
    CREATED = "created", _("Created")
    PROCESSING = "processing", _("During the processing")
    COMPLETED = "completed", _("Completed")
    FAILED = "failed", _("Failed")
