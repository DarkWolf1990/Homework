from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import FileForm


# Create your views here.
def good_prod(request, good):
    if request == 'GET':
        if good == 'goods':
            return render(request, 'goods/goods.html')
    else:
        return f"this error"

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             upload = form.cleaned_data['upload']
#             fs = FileSystemStorage()
#             fs.save(upload.name, upload)
#     else:
#         form = FileForm()
#     return render(request, 'goods/upload_file.html', {'form': form})
