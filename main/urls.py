from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', viewabout, name='about'),
    path('contacts/', viewcontacts, name='contacts'),
    path('login/', LoginView.as_view(), name='login'),
    path('service/', ProductList.as_view(), name='service'),
    path('create_service/', CreateProduct.as_view(), name='create_service'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)