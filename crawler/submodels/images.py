from django.db import models
from ImageCrawler.utils.choices import choices
from crawler.utils.image_status import ImageStatus
from crawler.submodels.baseurl import BaseUrl


class ImageUrl(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.CharField(null=False, blank=False, max_length=100)
    base_url_id = models.ForeignKey(BaseUrl, on_delete=models.PROTECT)
    status = models.IntegerField(choices=choices(ImageStatus), default=ImageStatus.active)
    updated_at = models.DateTimeField(auto_now_add=True)