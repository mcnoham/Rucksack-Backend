from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    api_get_user,
    api_create_user,
    ProfileView,
    api_create_itinerary,
    api_get_itinerary,
    delete_auth_token,
    filterView,
    delete_user,
    edit_profile,
    update_email,
    update_password,
    api_quick_search
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #GET requests
    path('get_user/<str:username>', api_get_user, name="get user"),
    path('<str:username>', ProfileView, name="Profile View"),
    path('quick_search/', api_quick_search),
    path('quick_search/<keyword>', api_quick_search),

    #POST requests
    path('filter_view/', filterView, ),
    path('user_create/<str:username>', api_create_user, name="create user"), 
    path('logout/', delete_auth_token, name="logout"), 
    path('login/',  obtain_auth_token, ), 
    path('create_itinerary/', api_create_itinerary, name="create itinerary"),
    path('delete_user/<user_id>',  delete_user, ),

    #PUT requests
    path('update_email/<username>',  update_email, ),
    path('update_password/<username>',  update_password, ),
    path('edit_profile/<user_id>',  edit_profile, )
]