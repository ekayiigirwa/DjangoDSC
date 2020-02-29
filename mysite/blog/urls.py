from django.urls import path
from . import views
#pk is a unique id for each post model we have
#post/<int:pk>/ specifies a URL pattern – we will explain it for you:
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

