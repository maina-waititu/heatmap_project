from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import healthFacilities
import json, ast
from django.template import RequestContext

#Registration
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

#check username if taken
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'world/index.html')

def home(request):
    return render(request, 'world/home.html')

def default(request):
    return render(request, 'world/default.html')

def query(request):
    return render(request, 'world/query.html')

def test(request):
    return render(request, 'world/test.html')

class SignUPView(CreateView):
    template_name = "world/signup.html"
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


class healthView(generic.ListView):
    # class meta:
    model = healthFacilities
    # properties = ('f_name', 'prov')
    # fields = ('f_name', 'prov', 'lat', 'long', 'f_type', 'geom')
    context_object_name = 'default'
    template_name = 'world/default.html'

    def points_view(request):
        #lookup point data
        points_as_geojson = serialize('geojson', healthFacilities.objects.pythall(), geometry_field= 'geom', properties=('f_name','prov','lat','long','f_type','geom'))
       #remove crs key because it is not recommended by http://geojsonlint.com/
        new_points_as_geojson = json.loads(points_as_geojson)
        new_points_as_geojson.pop('crs', None)
        new_points_as_geojson = json.dumps(new_points_as_geojson)
        return request.render_to_response({
            'new_points_as_geojson': new_points_as_geojson
        })

        # return HttpResponse(new_points_as_geojson, content_type='json')

class healthViewQuery(generic.ListView):
    # class meta:
    model = healthFacilities
    context_object_name = 'central_health'
    template_name = 'world/test.html'

    def central_facilities(request):
        # if request.POST.get("aoi-choice"):

            pointdata = serialize('geojson', healthFacilities.objects.filter(prov__iexact= "CENTRAL"))
            # request.POST.get("aoi-choice")
            new_points = json.loads(pointdata)
            new_points.pop('crs', None)
            new_points = json.dumps(new_points)

            response = HttpResponse(new_points, content_type='application/json')
            response['content-Disposition'] = 'attachment; filename="central_health_facilities.geojson"'

            #return HttpResponse(new_points, content_type='application/json')

## filter by county
class healthViewFilter(generic.ListView):
    # class meta:
    model = healthFacilities
    context_object_name = 'health_filter'
    template_name = 'world/default.html'

    def facilities_filter(request):
        if request.POST.get("aoi-choice"):
            pointdata = serialize('geojson', healthFacilities.objects.filter(name=request.POST.get("aoi-choice")))
            # request.POST.get("aoi-choice")
            new_points = json.loads(pointdata)
            new_points.pop('crs', None)
            new_points = json.dumps(new_points)

            return HttpResponse(new_points, content_type='json')

# def data_health(request):
#     health=serialize('geojson', healthFacilities.geom.all())
#     return HttpResponse(request, health, content_type='json')

# def get_health_data(request):
#     health = serialize('geojson', healthFacilities.objects.all(),
#           geometry_field= 'geom',
#           fields=('f_name', 'f_type', 'prov', 'dist', 'division', 'location', 'sub-locati'))
#     return HttpResponse(health, content_type='json')