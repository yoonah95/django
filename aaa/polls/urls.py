
from django.conf.urls import url, include

from rest_framework import routers




from . import views


router = routers.DefaultRouter()
router.register(r'signs', views.SignViewSet)
 
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^polls-v1/', include('rest_framework.urls', namespace='rest_framework_category')),
]
