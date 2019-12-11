from django.urls import path
from django.contrib import admin
from shops import views

urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', views.Home.as_view()),
]