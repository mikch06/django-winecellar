from django.urls import path, include

from wine.views import WineListView, WineDeleteView
from wine.views import WineDetailView
from wine.views import WineUpdateView
from wine.views import WineNewView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wine/', WineListView.as_view(), name='wine_list'),
    path('wine/<int:pk>', WineDetailView.as_view(), name='wine_detail'),
    path('edit/<int:pk>', WineUpdateView.as_view(), name='wine_edit'),
    path('delete/<int:pk>', WineDeleteView.as_view(), name='wine_delete'),
    path('about/', views.about, name='about'),

    ##  path('new/<int:pk>', WineNewView.as_view(), name='wine_edit'), # Create entries

    # watson search engine
    #path('r"^search/"', include('watson.urls')),
]
