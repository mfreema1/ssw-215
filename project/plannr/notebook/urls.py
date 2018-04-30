from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#map our index function to the root of our notebook app 
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('daily/', views.DailyListView.as_view(), name='daily_list'),
    path('daily/add', views.add_daily_entry, name='daily_entry_add'),
    path('daily/<int:pk>', views.DailyDetailView.as_view(), name='daily_detail'),
    path('weekly/', views.WeeklyListView.as_view(), name='weekly_list'),
    path('weekly/add', views.add_weekly_entry, name='weekly_entry_add'),
    path('weekly/<int:pk>', views.WeeklyDetailView.as_view(), name='weekly_detail'),
    #path('monthly/', views.MonthlyListView.as_view(), name='monthly_list'),
    #path('monthly/<int:pk>', views.MonthlyDetailView.as_view(), name='monthly_detail'),
]