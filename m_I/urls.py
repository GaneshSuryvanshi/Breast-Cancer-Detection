from django.urls import path
from m_I import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('input/home/',views.homepage1,name='homepage'),
    path('input/',views.user_input,name='forms'),
    path('input/home/input/',views.user_input,name='forms'),
    path('input/home/input/predicting',views.user_input_final,name='final'),
    path('input/predicting',views.user_input_final,name='final'),
    
]