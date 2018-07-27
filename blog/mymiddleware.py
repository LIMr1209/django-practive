from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class SpiderMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        http_user_agent = request.META.get('HTTP_USER_AGENT')
        print(http_user_agent)
        http_user_agent = str(http_user_agent).lower()
        if 'py' in http_user_agent:
            return HttpResponse('滚蛋,小爬虫')

    def process_response(self, request, response):
        return response
