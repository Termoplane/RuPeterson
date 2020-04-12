from django.urls import path


from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='blog'),
    path('entry/<int:pk>/', views.EntryView.as_view(), name='entry'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
    path('donate/', views.donate, name='donate'),
    
]