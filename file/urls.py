from django.urls import path, include
from .views import FileUploadView, FileRetreiveView

app_name = 'file'
urlpatterns = [
    path('file/', FileUploadView.as_view()),
    path('file/medium/', FileRetreiveView.as_view())
]
