from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Url
from .serializers import UrlSerializer
from django.views import View
from django.conf import settings

# This class manages the GET request from the client and give all model objects as a response.
class ShortenerListApiView(ListAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


# This class manages the POST request from the client and responsible to save "original_url" and "short_url" in the database. 
class ShortenerCreateApiView(CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


# This class is resposible to redirect the "short_url" to "original_url" when client hits "short_url" in the browser.
class Redirect(View):
    def get(self,request,short_url,*args,**kwargs):
        link = settings.HOST_URL + '/' + short_url
        redirect_link = Url.objects.get(short_url=link).original_url
        return redirect(redirect_link)
