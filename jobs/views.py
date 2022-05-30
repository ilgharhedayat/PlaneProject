from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Job
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.urls import reverse


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'jobs/list.html'
    context_object_name = 'category_list'


class JobListView(ListView):
    def get_queryset(self, *args, **kwargs):
        job_list = get_list_or_404(Job, category_id=kwargs.get('id'))
        return job_list


class JobDetailView(FormMixin, DetailView):
    model = Job
    template_name = ''
    slug_field = 'id'
    slug_url_kwarg = 'id'
    form_class = ''

    def get_success_url(self):
        return reverse('', kwargs={'id': self.object.id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        apply = form.save()
        apply.job = self.get_object()
        apply.save()
        messages.success(self.request, '', '')
        return super(JobDetailView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(JobDetailView, self).form_invalid(form)
