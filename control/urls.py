from django.urls import path
from .views import SignUp, SignIn, SignOut


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', SignUp.as_view(), name='signup'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('logout/', SignOut.as_view(), name='signout'),
]