from django.db import models
from crawler.submodels.baseurl import BaseUrl


class BaseUrlManager(models.Manager):

    @classmethod
    def add_url(cls, url, depth):
        print(url+" "+str(depth))
        result = BaseUrl()
        result.base_url = url
        result.depth = depth
        result.save()
        print (result)
        return True, result.id




