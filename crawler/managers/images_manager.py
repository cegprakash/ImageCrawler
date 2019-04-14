from django.core.paginator import Paginator
from django.db import models

from ImageCrawler.utils.common import get_dict
from crawler.submodels.images import ImageUrl


class ImagesManager(models.Manager):

    @classmethod
    def add_url(cls, image_url, base_url_obj):
        result = ImageUrl()
        result.base_url_id = base_url_obj
        result.image_url = image_url
        result.save()
        return True, result.id

    @classmethod
    def get_urls(cls, request, id):
        data = ImageUrl.objects.filter(base_url_id=id)
        paginator = Paginator(data, 20)  # Show 20 urls per page
        page = request.GET.get('page')
        results = paginator.get_page(page)

        converted = []
        for result in results:
            converted.append(get_dict(result.__dict__))

        data = {}

        data['total_pages'] = paginator.num_pages
        data['results_per_page'] = paginator.per_page
        data['data'] = converted

        print(data)
        return True, data