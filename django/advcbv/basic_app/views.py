from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return render(request, 'index.html')
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based Views are cool!")
class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION!'
    #     return context

class SchoolListView(ListView):
    context_object_name = 'schools'# default returns object with name 'school_list' (lowercases everything and adds _List to the name)
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'# default returns object with name 'school' (lowercases everything)
    model = models.School
    template_name = 'basic_app/school_detail.html'


# class SchoolCreateView(CreateView):
#     model = models.School



class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
