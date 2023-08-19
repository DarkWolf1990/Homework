import logging
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Accommodation
from .models import ListOfCountries

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


def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }
    return render(request, 'home/accommodation_details.html', content)
