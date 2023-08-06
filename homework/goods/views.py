from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import ImageForm


# Create your views here.
def goods(request):
    return render(request, 'goods/goods.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.cleaned_data['upload']
            fs = FileSystemStorage()
            fs.save(upload.name, upload)
    else:
        form = ImageForm()
    return render(request, 'goods/upload_image.html', {'form': form})
