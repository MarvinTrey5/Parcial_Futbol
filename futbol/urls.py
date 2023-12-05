from django.urls import path
from.views_api import APi_Clas,APi_Clas2,APi_Clas3, InicioView


urlpatterns = [
    path('api/', APi_Clas.as_view(), name='api_view1'),
    path('api2/',APi_Clas2.as_view(), name='api_view2'),
    path('api3/',APi_Clas3.as_view(), name='api_view3'),
    path('',InicioView.as_view(), name='inicio_view'),
]