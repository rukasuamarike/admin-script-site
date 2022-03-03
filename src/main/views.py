from django.http import Http404,request
from django.shortcuts import render,get_object_or_404,redirect
import logging

logger = logging.getLogger(__name__)
#logger2 = logging.getLogger(‘django.request’)

# Create your views here.
def home_view(request):

    logging.config.dictConfig({
        'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
    })
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    logger.error("Test!!")
    context = {
        'visits': num_visits,
    }

    return render(request, "main/home.html",context)

def console_view(request):
    return render(request, "main/console.html")