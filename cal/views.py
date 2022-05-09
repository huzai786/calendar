from django.shortcuts import render
from .models import Filter, EventDetails, Token, Calenders
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from .forms import CreateEventForm
from django.urls import reverse_lazy

def home(request):
    events = EventDetails.objects.all()


    context = {'events': events}
    return render(request, 'cal/home.html', context)


def filter_config(request):
    filters = Filter.objects.all()

    context = {'filters': filters}
    return render(request, 'cal/filter_config.html', context)


def manage_account(request):
    emails = Token.objects.all()


    context = {'emails': emails}
    return render(request, 'cal/manage_account.html', context)

def add_event(request):
    form = CreateEventForm()
    context = {'form': form}
    return render(request, 'cal/forms.html', context)

class DetailAccount(DetailView):
    model = Token
    template_name = 'cal/manage_account.html'
    context_object_name = 'emails'


class EditAccount(UpdateView):
    model = Token
    template_name = 'cal/edit_account.html'
    fields = '__all__'
    success_url = reverse_lazy('account-detail')

class DeleteAccount(DeleteView):
    model = Token
    template_name = 'cal/delete_account.html'
    success_url = reverse_lazy('account-detail')

class CreateAccount(CreateView):
    model = Token
    fields = '__all__'
    template_name = 'cal/create_account.html'
    success_url = reverse_lazy('account-detail')