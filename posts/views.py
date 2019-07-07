from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models
from braces.views import SelectRelatedMixin
from django.urls import reverse


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username_iexact=self.kwargs.get('username'))
