from django.urls import path
from django.urls import path
from . import views
from neibour import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile,name = 'profile'),
    path('update_profile/', user_views.update_profile,name = 'update_profile'),
    path('new_hood/', views.new_hood, name='new_hood'),
    path('hood/', views.neighbourhood, name = 'hood'),
    path('edithood/', views.edit_hood, name= 'edithood')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)