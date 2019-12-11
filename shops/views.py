from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)


def index(request):
    template = loader.get_template('shops/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
                                                       user_location)
                                     ).order_by('distance')[0:99]
    template_name = 'shops/index.html'
