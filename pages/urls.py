from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path(
        'home/',
        views.index,
        name='home',
        ),
    path(
        'post/',
        views.postView,
        name="post",
    ),
    path(
        'post/all/',
        views.allPost,
        name='allpost',
    ),
    path(
        'post/my/',
        views.myPost,
        name='mypost'
    )
]