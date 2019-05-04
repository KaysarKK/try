from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:city_id>/', views.detail_city, name='detail_city'),

    path('<int:city_id>/<int:device_id>/', views.detail_city_inside, name='detail_city_inside'),

    path('data/', views.data, name='data'),

    path('download/', views.download, name='download'),

    path('graph/', views.graph, name='graph'),

    path('graph2/', views.graph2, name='graph2'),
]