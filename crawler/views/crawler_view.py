from unittest.mock import Base

from crawler.serializers.crawl_serializer import CrawlSerializer
from rest_framework.response import Response
from ImageCrawler.utils.format_form_errors import format_form_errors
import ImageCrawler.utils.json_response as Response
from rest_framework import generics
from rest_framework import status
from crawler.managers.baseurl_manager import BaseUrlManager
from crawler.services.crawl_service import CrawlService

class CrawlerView(generics.GenericAPIView):
    serializer_class = CrawlSerializer

    def post(self, request):
        serializer = CrawlSerializer(data=request.data)

        if not serializer.is_valid():
            return Response.error_response(errors=format_form_errors(serializer.errors.items()))

        success, data = CrawlService.execute(serializer.validated_data)

        if success:
            return Response.success_response(message="created", data=data, code=status.HTTP_201_CREATED)
        else:
            return Response.error_response(
                message=data['message'] if 'message' in data else None,
                errors=format_form_errors(data['errors'].items()) if 'errors' in data else None,
                code=data['code'] if 'code' in data else status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def get(self, request):

        success, data = BaseUrlManager.get_urls(request)

        if success:
            return Response.success_response(message="", data=data, code=status.HTTP_200_OK)
        else:
            return Response.error_response(
                message=data['message'] if 'message' in data else None,
                errors=format_form_errors(data['errors'].items()) if 'errors' in data else None,
                code=data['code'] if 'code' in data else status.HTTP_500_INTERNAL_SERVER_ERROR
            )