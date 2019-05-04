from django.urls import include, path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('city/', views.CityList.as_view()),
    path('device/', views.DeviceList.as_view()),
    path('info/', views.InfoList.as_view()),
]

