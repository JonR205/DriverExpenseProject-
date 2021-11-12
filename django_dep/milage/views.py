from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)
from .models import Post
from .forms import PostMilageForm

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'milage/home.html', context, )


class PostListView(ListView):
    model = Post
    template_name = 'milage/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_driven']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostMilageForm
    template_name = 'milage/post_form.html'
    # fields = ['title', 'miles', 'date_driven']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# def post(request):
#     form = PostMilageForm(request.POST)
#     return render(request, 'milage/post_form.html', {'form': form})


def about(request):
    return render(request,'milage/about.html', {'title': 'About'})


