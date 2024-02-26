from django.shortcuts import render

# Create your views here.


def file_form_view(request, *args, **kwargs):
    return render(request, "upload_form.html")
