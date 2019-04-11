from crawler.managers.baseurl_manager import BaseUrlManager


class CrawlService:

    @classmethod
    def execute(cls, data):
        try:
            success, result = BaseUrlManager.add_url(data['url'], data['depth'])
            return success, result
        except Exception as e:
            return False, str(e)

