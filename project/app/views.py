from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Url
from .serializers import UrlSerializer
from django.views import View
from django.conf import settings


class ShortenerListApiView(ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class ShortenerCreateApiView(CreateAPIView):
    serializer_class = UrlSerializer


class Redirect(View):
    def get(self,request,short_url,*args,**kwargs):
        link = settings.HOST_URL + '/' + short_url
        redirect_link = Url.objects.get(short_url=link).original_url
        return redirect(redirect_link)
