from django.urls import path
from . import views

urlpatterns = [
    path('api/cookies', views.CookieList.as_view(), name='cookie_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/cookies/<int:pk>', views.CookieDetail.as_view(), name='cookie_detail'), # api/contacts will be routed to the ContactDetail view for handling
]