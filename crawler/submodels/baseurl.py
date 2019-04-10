from django.db import models
from ImageCrawler.utils.choices import choices
from crawler.utils.base_url_status import BaseUrlStatus


class BaseUrl(models.Model):
    id = models.AutoField(primary_key=True)
    base_url = models.CharField(null=False, blank=False, max_length=100)
    status = models.IntegerField(choices=choices(BaseUrlStatus), default=BaseUrlStatus.active)
    updated_at = models.DateTimeField(auto_now_add=True)

