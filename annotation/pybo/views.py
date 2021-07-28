from django.http import HttpResponse

def index(request):
    return HttpResponse("장고 기본 설정")