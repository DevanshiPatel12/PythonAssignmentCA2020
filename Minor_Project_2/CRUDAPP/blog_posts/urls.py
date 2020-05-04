from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_create, name='blog_insert'),    # get and post req. for insert operation
    path('<int:id>/', views.blog_create, name='blog_update'), # get and post req. for update operation
    path('list/', views.blog_list,name='blog_list'),    # get req. to retrieve and display all records
    path('delete/<int:id>/', views.blog_delete, name='blog_delete'),
]

