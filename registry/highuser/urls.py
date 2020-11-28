from django.urls import path
from . import views
urlpatterns=[
    path('',views.approveUser,name='approveUser'),
    path('appuser/<int:userdb_aad>/',views.viewuser,name='viewuser'),
    path('deleteuser/<int:userdb_aad>',views.deleteuser,name='deleteuser'),
    path('adminhome/',views.adminhome,name='adminview'),
    path('reportuser/',views.reportuser,name='reportuser'),
]
