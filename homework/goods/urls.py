from django.urls import path
from .views import goods, upload_image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('goods/', goods, name='goods'),
    path('upload/', upload_image, name='upload_image'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
