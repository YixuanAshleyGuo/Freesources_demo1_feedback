from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.
def index(request):
#    map_1 = folium.Map(location=[45.372, -121.6972], title = 'Stamen Terrain')
#    map_1.simple_marker([45.3288, - 121.6625], popup='Mt. Hood Meadows')
#    map_1.simple_marker([45.3311, -121.7113], popup='Timberline Lodge')
#    map_1.create_map(path='mthood.html')
    return render(request,'feedback/index.html')