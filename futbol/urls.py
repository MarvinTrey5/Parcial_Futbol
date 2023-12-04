from django.urls import path
from.views_api import APi_Clas,APi_Clas2,APi_Clas3, InicioView


urlpatterns = [
    path('api/', APi_Clas.as_view()),
    path('api1/',APi_Clas2.as_view()),
    path('api2/',APi_Clas3.as_view()),
    path('',InicioView.as_view()),
]