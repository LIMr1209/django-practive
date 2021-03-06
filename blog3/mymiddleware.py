from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class SpiderMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        http_user_agent = request.META.get('HTTP_USER_AGENT')
        http_user_agent = str(http_user_agent).lower()
        if 'py' in http_user_agent:
            return HttpResponse('滚蛋，小爬虫')

    def process_response(self, request, response):
        return response
