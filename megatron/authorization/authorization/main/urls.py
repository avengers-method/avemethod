from django.urls import re_path, path, include
from main.routers import router
from main.views import ChangePasswordView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'users/\d+/change_password/$', ChangePasswordView.as_view())
]
