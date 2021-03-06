from django.db import models
from django.utils import timezone
# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=200)
    main = models.BooleanField()
    text = models.TextField()
    image = models.ImageField(upload_to='uploads')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


