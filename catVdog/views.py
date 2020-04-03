import os

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from catVdog.models import Img
from catVdog.utils import predict


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload_img(request):
    dir_path = os.path.join(settings.MEDIA_ROOT, 'img')
    for file in os.listdir(dir_path):
        target_file = os.path.join(dir_path, file)
        if os.path.isfile(target_file):
            os.remove(target_file)
    uploaded = False
    if request.method == 'POST':
        file = request.FILES.get('img', None)
        if file:
            new_img = Img(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name
            )
            new_img.save()
            uploaded = True
    return render(request, 'uploadimg.html', {'uploaded': uploaded})


def result(request):
    return render(request, 'result.html', {"data": predict()})
