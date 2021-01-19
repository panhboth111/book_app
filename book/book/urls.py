
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sales.views import BookViewset

router = DefaultRouter()
router.register('sales', BookViewset, )

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/', include(router.urls))
]
