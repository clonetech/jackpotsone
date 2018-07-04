from django.urls import path
from django.conf import settings
from . views import home, punter, hexabet, payment, results, jackpot, welcome, signup
from . import views
from . import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'jackpot'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('punter/', views.punter, name='punter'),
    path('hexabet/', views.hexabet, name='hexabet'),
    path('payment/', views.payment, name='payment'),
    path('results/', views.results, name='results'),
    path('jackpot/', views.jackpot, name='jackpot'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', core_views.signup, name='signup'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
