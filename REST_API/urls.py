from django.urls import path
from .views import home, sys_admin, sys_admin_details


urlpatterns = [
    path('', home),  # My custom homepage, instead of the default Django landing page.
    # Getting the api view in product/.
    path('sysadmin/', sys_admin),
    path('sysadmin/<int:pk>', sys_admin_details)
]
