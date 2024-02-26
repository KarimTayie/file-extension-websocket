from django.urls import path

from . import views

app_name = "file_extension"

urlpatterns = [
    path("upload/", views.file_form_view, name="file_form"),
]
