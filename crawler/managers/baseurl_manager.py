from django.core.paginator import Paginator
from django.db import models

from ImageCrawler.utils.common import get_dict
from crawler.submodels.baseurl import BaseUrl
from crawler.utils.base_url_status import BaseUrlStatus


class BaseUrlManager(models.Manager):

    @classmethod
    def add_url(cls, url, depth):
        result = BaseUrl()
        result.base_url = url
        result.depth = depth
        result.save()
        return True, result.id

    @classmethod
    def get_url_to_process(cls):
        data = BaseUrl.objects.filter(status=BaseUrlStatus.unprocessed).order_by('updated_at').first()
        return data

    @classmethod
    def get_urls(cls, request):
        data = BaseUrl.objects.all()
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

        return True, data
