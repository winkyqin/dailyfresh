from django.conf.urls import url
from apps.user.views import RegisterView

app_name = "user"
urlpatterns = [
    url('^register$', RegisterView.as_view(), name="register"),
]
