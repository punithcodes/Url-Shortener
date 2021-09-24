from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortenerListApiView.as_view(), name='all_urls'),
    path('create/', views.ShortenerCreateApiView.as_view(), name='create_link'),
    path('<str:short_url>', views.Redirect.as_view(), name='redirect'),
]
