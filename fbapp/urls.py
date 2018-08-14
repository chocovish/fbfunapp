from django.urls import path
from .views import home, info, results,detail,tnc
from .utilities import resultimg


urlpatterns = [
    path("", home),
    path("app/results/<pk>/", results, name='results'),
    path("app/<pk>/",detail, name="detail"),
    path("app/<pk>/result/",resultimg, name="result"),
    path("app/<pk>/info/",info),
    path("tnc/",tnc)
]