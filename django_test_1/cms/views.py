from django.http import HttpResponse

def htsy(request):
    return HttpResponse('后台首页')

def htdlym(request):
    return HttpResponse('后台登录页面')

