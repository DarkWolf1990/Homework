from django.urls import path
from goods import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.good_prod, name='good_prod')
    # path('upload/', views.upload_file, name='upload_file'),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
