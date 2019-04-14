from django.contrib import admin
from django.urls import path, include
import crawler
from crawler import urls

from crawler.views.crawler_view import CrawlerView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path(r'', schema_view),
    path(r'api/', include(crawler.urls)),

    #path(r'admin/', admin.site.urls),
]
