from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    isVideo = models.BooleanField(default=False)
    # uploaded_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.file.name
