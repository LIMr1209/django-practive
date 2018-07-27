from django.utils.deprecation import MiddlewareMixin


class SpiderMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        a = request.META.get('')

    def process_response(self, request, response):
        pass
