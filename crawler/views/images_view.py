from unittest.mock import Base

from crawler.serializers.images_serializer import ImagesSerializer
from rest_framework.response import Response
from ImageCrawler.utils.format_form_errors import format_form_errors
import ImageCrawler.utils.json_response as Response
from rest_framework import generics
from rest_framework import status
from crawler.managers.images_manager import ImagesManager


class ImagesView(generics.GenericAPIView):
    serializer_class = ImagesSerializer

    def get(self, request, id):

        success, data = ImagesManager.get_urls(request, id)

        if success:
            return Response.success_response(message="", data=data, code=status.HTTP_200_OK)
        else:
            return Response.error_response(
                message=data['message'] if 'message' in data else None,
                errors=format_form_errors(data['errors'].items()) if 'errors' in data else None,
                code=data['code'] if 'code' in data else status.HTTP_500_INTERNAL_SERVER_ERROR
            )