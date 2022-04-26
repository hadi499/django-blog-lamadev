from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import PostForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


# def create(request):
#     post_form = PostForm(request.POST, request.FILES)

#     if request.method == 'POST':
#         if post_form.is_valid():
#             post_form.save()

#         return redirect('home')

#     return render(request, 'blog/create.html')


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
