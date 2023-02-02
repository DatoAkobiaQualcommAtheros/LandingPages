from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
