from django.urls import path
from django.conf.urls import include
# Views
from .views import PersonView, CommonsView, CommonsViewDetail, ServerView

urlpatterns = [
    path('api/fc/', PersonView.as_view()),
    path('api/commons/', CommonsView.as_view()),
    path('api/commons/<str:code>/', CommonsViewDetail.as_view()),
    path('api/server/', ServerView.as_view()),
]
