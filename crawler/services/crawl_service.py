from crawler.managers.crawl_manager import CrawlManager


class CrawlService:

    @classmethod
    def execute(cls, data):
        try:
            print(data['url'])
            print(data['depth'])
            # res = CrawlManager.reset_password(data['user_id'], data['code'], make_password(data['password'], None))
            return True, ""
        except Exception as e:
            return False, str(e)

