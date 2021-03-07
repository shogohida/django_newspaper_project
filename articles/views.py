# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list_html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail_html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_update_html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete_html'
    success_url = reverse_lazy('article_list')