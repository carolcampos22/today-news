from django.urls import path
from rest_api.views import hello_world
from rest_framework.routers import SimpleRouter
from rest_api.views import NewsModelViewset


app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('news', NewsModelViewset)

urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),      
]

urlpatterns +=  router.urls