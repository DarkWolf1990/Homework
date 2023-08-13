import logging
from django.shortcuts import render

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
