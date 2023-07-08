from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Dulcinea
from .forms import DulcineaForm
from django.urls import reverse_lazy

# Create your views here.



class Homeview(ListView):
      model = Dulcinea
      template_name = 'home.html'
      ordering = ['-date_1']


      


class ExpensesView(ListView):
      model = Dulcinea
      template_name = 'expenses.html'

class EventDetailView(DetailView):
      model = Dulcinea
      template_name = 'event_detail.html'

class AddEventView(CreateView):
      model = Dulcinea
      form_class = DulcineaForm
      template_name = 'add_event.html'
      # fields = '__all__'
      # one can also pass field in this way:
      #fields = ('date_1','desc', 'RS_rate', 'GM_rate')

class UpdateEventView(UpdateView):
      model = Dulcinea
      template_name = 'update_events.html'
      fields = ['date_1','desc', 'RS_rate', 'GM_rate', 'event_image']

class DeleteEventView(DeleteView):
      model = Dulcinea
      template_name = 'delete_event.html'
      success_url = reverse_lazy('home')

