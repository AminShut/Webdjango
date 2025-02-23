from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Post,Comment
from .forms import CommentForm, PostForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# class BlogListView(ListView):
#     model = Post
#     template_name = 'blog/list.html'
#     context_object_name = 'posts'

def blog_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/list.html', context)

# class BlogDetailView(DetailView, FormMixin):
#     model = Post
#     template_name = 'blog/detail.html'
#     context_object_name = 'post'
#     form_class = CommentForm

    # def get_success_url(self):
    #     return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailView,self).get_context_data(**kwargs)
    #     context['form'] = CommentForm(initial={'post': self.object, 'author': self.request.user})
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         pass
    
    # def form_valid(self, form):
    #     form.save()
    #     return super(BlogDetailView,self).form_valid(form)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.post = post
            obj.save()

            return redirect(reverse_lazy('blog_detail', kwargs={'pk': post.id}))
    else:
        form = CommentForm()
    
    return render(request, 'blog/detail.html', {'post': post, 'form': form})

    

# class BlogEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#     model = Post
#     template_name = 'blog/edit.html'
#     context_object_name = 'post'
#     fields = [
#         'title',
#         'text',
#     ]

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST or None, instance = post)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('blog_detail', kwargs={'pk': post.id}))
            
        else:
            form = PostForm(instance = post)
            return render(request, 'blog/edit.html', {'form' : form, 'post' : post})

    else:
        return HttpResponseForbidden()

        
        

# class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
#     model = Post
#     template_name = 'blog/delete.html'
#     context_object_name = 'post'
#     success_url = reverse_lazy('blog_list')

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect(reverse_lazy('blog_list'))
        else:
            return render(request, 'blog/delete.html', {'post' : post})
    else:
        return HttpResponseForbidden()


# class BlogCreatView(LoginRequiredMixin,CreateView):
#     model = Post
#     template_name = 'blog/add.html'
#     context_object_name = 'post'
#     fields=[
#         'title',
#         'text',
#     ]

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

@login_required
def blog_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect(reverse_lazy('blog_detail', kwargs={'pk': obj.id}))
    else:
        form = PostForm()
    return render(request, 'blog/add.html', {'form': form})