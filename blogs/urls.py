from django.urls import path
from .views import home_view,post_view, create_view,base_view,author_view,blog_detail

app_name = 'blogs'

urlpatterns=[
    path('',home_view, name='homepage'),
    path('post/',post_view,name='blog'),
    path('create/',create_view, name='create_blog'),
    path('authors/', author_view, name='authors'),
    path('detail/<int:blog_id>/',blog_detail,name='detail')
]
