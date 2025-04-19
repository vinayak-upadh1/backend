from django.urls import path
from .views import (
    UserFileCreateView,
    UserFileListView,
    UserFileRetrieveUpdateView,
    UserFileDeleteView,
)

urlpatterns = [
    path("files/", UserFileListView.as_view(), name="userfile-list"),
    path("files/upload/", UserFileCreateView.as_view(), name="userfile-create"),
    path("files/<str:pk>/", UserFileRetrieveUpdateView.as_view(), name="userfile-detail"),
    path("files/delete/<str:pk>/", UserFileDeleteView.as_view(), name="userfile-delete"),
]
