from django.urls import path
from . import views
from .views import Homeview, EventDetailView, ExpensesView, AddEventView, UpdateEventView, DeleteEventView

urlpatterns = [
   #path('', views.home, name='home')
   path('', Homeview.as_view(), name='home'),
   path('event_detail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
   path('add_event/', AddEventView.as_view(), name='add-event'),
   path('expenses/', ExpensesView.as_view(), name='expenses'),
   path('update_event/<int:pk>', UpdateEventView.as_view(), name='update-detail'),
   path('delete_event/<int:pk>/delete', DeleteEventView.as_view(), name='delete-event'),
]
