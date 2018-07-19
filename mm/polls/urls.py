router = routers.DefaultRouter()
router.register(r'versions',views.VersionViewSet)

urlpatterns = [
     url(r'^',include(router.urls)),
     url(r'^api-v1/',include('rest_framework.urls',namespace='rest_framework_category')),

     ]
