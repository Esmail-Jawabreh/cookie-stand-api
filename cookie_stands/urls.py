from django.urls import path
from .views import Cookie_standList, Cookie_standDetail

urlpatterns = [
    path("", Cookie_standList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", Cookie_standDetail.as_view(), name="cookie_stand_detail"),
]
