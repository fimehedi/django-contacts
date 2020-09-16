from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Contact


# Global Variable
fields = ['name', 'email', 'phone', 'info', 'gender', 'image',]


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)


class ContactDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Contact
    template_name = 'detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.manager == self.request.user


@login_required
def search(request):
    if request.GET['search_term'].strip():
        search_term = request.GET['search_term']
        search_result = Contact.objects.filter(manager=request.user).filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__icontains=search_term)
        )
        context = {
            'search_term' : search_term,
            'contacts' : search_result
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "create.html"
    fields = fields

    def form_valid(self, form):
        form.instance.manager = self.request.user
        messages.success(self.request, 'Your contact successfully created!')
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    template_name = "update.html"
    fields = fields

    def test_func(self):
        obj = self.get_object()
        return obj.manager == self.request.user

    def form_valid(self, form):
        form.instance.manager = self.request.user
        messages.success(self.request, 'Your contact successfully updated!')
        return super().form_valid(form)


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    template_name = "delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.manager == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your contact successfully deleted!')
        return super().delete(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')






