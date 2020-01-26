from django.conf.urls import url
from  django.urls import include, path, re_path
from .import views
from djgeojson.views import GeoJSONLayerView

from .models import healthFacilities

app_name = 'world'

urlpatterns = [
    path('signup/', views.SignUPView.as_view(), name='signup'),
    path('world/validate_username', views.validate_username, name='validate_username'),
    path('', views.healthView.as_view(), name='default'),
    path('', views.healthViewFilter.as_view(), name='health_filter'),
    path('test.html', views.healthViewQuery.as_view(), name='central_health'),
    # path('central_hf.geojson', views.healthViewQuery.as_view(), name='central_health_f'),
    # path('', views.healthViewQuery.as_view(), name='central_health_f'),
    # path('home.html', views.healthView.as_view(), name='home'),
    # path('points', views.healthView.points_view, name='default'),
    path('central.geojson', views.healthViewQuery.central_facilities, name='central_health'),
    path('health.geojson', GeoJSONLayerView.as_view(model=healthFacilities, properties=('f_name', 'f_type', 'prov')), name='health')
    # path('world/', views.WorldDetailView.as_view(), name='world-detail'),

]

