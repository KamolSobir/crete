from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import HomeList, CommentView, CreateList, PostDeleteView, PostUpdateView, Register, AvtorView, Myproject, MyDetail, PhotoCreates

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('create/', CreateList.as_view(), name='creates'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('login/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name="register"),
    path('avtori/', AvtorView.as_view(), name='avtors'),
    path('my_project/', Myproject.as_view(), name='my_project'),
    path('photo_update/<int:pk>', PhotoUpdate.as_view(), name='photo_update'),
    path('photo_create/', PhotoCreates.as_view(), name='photo_create'),
    path('my_project_id/<int:id>/', MyDetail.as_view(), name='my_project_id'),
    path('subscribe/', subscribe_user, name="subscribe-post"),
    # path('subscribe/<int:pk>', subscribe_user, name="subscribe-post"),
    path('like-post/', like_post, name='like-post'),
    path('comment/<int:pk>/', CommentView.as_view(), name='post-comment'),

]
