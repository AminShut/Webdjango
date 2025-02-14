from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView, FormMixin):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView,self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object, 'author': self.request.user})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass
    
    def form_valid(self, form):
        form.save()
        return super(BlogDetailView,self).form_valid(form)


class BlogEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    context_object_name = 'post'
    fields = [
        'title',
        'text',
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogCreatView(LoginRequiredMixin,CreateView):
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