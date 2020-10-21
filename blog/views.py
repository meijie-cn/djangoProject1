from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Blog, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blog_list'  # variable name
    queryset = Blog.objects.all()  # get first 10 blogs
    template_name = 'blog_list.html'  # specify template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['nav_active'] = 'blogs'
        return context

class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['nav_active'] = 'blogs'
        return context

# Create your views here.
def index(request):
    num_blogs = Blog.objects.all().count()
    context = {"num_blogs": num_blogs,"nav_active":"home"}
    return render(request,
                  'index.html',
                  context)

def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    return render(
        request,
        'blog_detail.html',
        context={'blog': blog}
    )

def author_detail_view(request, pk):
    blog_list = Blog.objects.filter(author_id=pk)
    return render(
        request,
        'author_detail.html',
        context={'blog_list':blog_list,'nav_active':'blogs'}
    )
