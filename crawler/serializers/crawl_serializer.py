from rest_framework import serializers


class CrawlSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    depth = serializers.IntegerField(required=True, min_value=1, max_value=5)
