# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserFileViewSet

# router = DefaultRouter()
# # router.register(r'files', FileViewSet)
# router.register(r'files', UserFileViewSet, basename='files')

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('files/', UserFileViewSet.as_view())
# ] 

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
    path("files/<int:pk>/", UserFileRetrieveUpdateView.as_view(), name="userfile-detail"),
    path("files/<int:pk>/delete/", UserFileDeleteView.as_view(), name="userfile-delete"),
]
