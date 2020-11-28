from django.urls import path
from . import views
urlpatterns=[
    path('',views.register,name='reg'),
    path('aadharregistration/',views.aadharregistration,name='aadharregistration'),
    path('pancardregistration/',views.pancardregistration,name='pancardregistration'),
    path('passportregistration/',views.passportregistration,name='passportregistration'),
    path('votercardregistration/',views.votercardregistration,name='votercardregistration'),
    path('marriagecertregistration/',views.marriagecertregistration,name='marriagecertregistration'),
    path('licenseregistration/',views.licenseregistration,name='licenseregistration'),
    path('viewall/',views.viewall,name='viewall'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login'),
    path('edit/',views.editdetails,name='edit'),
    path('t_edit/',views.t_edit,name='t_edit'),
    path('home/',views.home,name='home'),
    ]