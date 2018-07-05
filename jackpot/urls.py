from .views import home
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views
from . import views as core_views
from django.contrib.auth import views as auth_views

app_name = 'jackpot'

urlpatterns = [

    path('home/', views.home, name='home'),
    path('punter/', views.punter, name='punter'),
    path('singlebet/', views.singlebet, name='singlebet'),
    path('hexabet/', views.hexabet, name='hexabet'),
    path('payment/', views.payment, name='payment'),
    path('results/', views.results, name='results'),
    path('jackpot/', views.jackpot, name='jackpot'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
