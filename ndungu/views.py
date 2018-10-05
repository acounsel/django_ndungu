from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from ndungu.models import Allocation, Province, Municipality, Authority, Entity

class Home(View):

    def get(self, request, **kwargs):
        return render(request, 'home.html')

class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

class MunicipalityList(BaseView, ListView):
    model = Municipality

class MunicipalityDetail(BaseView, DetailView):
    model = Municipality

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AllocationList(BaseView, ListView):
    model = Allocation

class AllocationDetail(BaseView, DetailView):
    model = Allocation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allocation_list'] = Allocation.objects.filter(municipality__allocation=context['allocation'])
        return context

class ProvinceList(BaseView, ListView):
    model = Province

class ProvinceDetail(BaseView, DetailView):
    model = Province

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allocation_list'] = Allocation.objects.filter(municipality__province=context['province'])
        return context

class AuthorityList(BaseView, ListView):
    model = Authority

class AuthorityDetail(BaseView, DetailView):
    model = Authority

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EntityList(BaseView, ListView):
    model = Entity

class EntityDetail(BaseView, DetailView):
    model = Entity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

