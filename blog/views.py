from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

class BlogEditView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    context_object_name = 'post'
    fields = [
        'title',
        'text',
    ]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog_list')

class BlogCreatView(CreateView):
    model = Post
    template_name = 'blog/add.html'
    context_object_name = 'post'
    fields=[
        'title',
        'text',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)