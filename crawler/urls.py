from django.urls import path
from crawler.views.crawler_view import CrawlerView
from crawler.views.images_view import ImagesView


urlpatterns = [
    path(r'crawl', CrawlerView.as_view()),
    path(r'crawled/<int:id>', ImagesView.as_view()),
]