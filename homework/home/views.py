import logging
from django.shortcuts import render
from .models import Accommodation
logger = logging.getLogger(__name__)


def get_page(request, page):
    if page == 'index':
        logger.info('Index page accessed')
        return render(request, 'home/home.html')
    elif page == 'about':
        logger.info('Index page accessed')
        return render(request, 'home/about.html')
    else:
        return f'Вы ввели не существующий адрес {page}!'


def accommodations(request):
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'home/accommodations.html', content)
