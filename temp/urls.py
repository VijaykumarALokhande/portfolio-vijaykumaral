from django.urls import path
from . import views
urlpatterns = [
    path('', views.fn, name='BLog_homi'),
    path('<int:blog_id>/', views.fnspacific, name='specific'),
]
