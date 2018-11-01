from django.urls import include, path
from . import views

app_name = 'investigaciones'

urlpatterns = [
    path('', views.index, name='index'),
    path('CC/', views.CC, name='CC'),
    path('CT/', views.CT, name='CT'),
    path('CN/', views.CN, name='CN'),
    path('CS/', views.CS, name='CS'),
    path('CM/', views.CM, name='CM'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
    path('crear/', views.crear, name='crear'),
]
