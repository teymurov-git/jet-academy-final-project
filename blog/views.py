from django.views.generic import ListView, DetailView
from blog.models import Blog
from django.shortcuts import render, get_object_or_404

# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'    # İstifadə olunacaq template
    context_object_name = 'blogs'  # Template-ə göndərilən dəyişən adı
    ordering = ['-created_at']     # İstəyə görə son əlavə olunanlar önə çəkilir
    paginate_by = 10


# def blog_details(request, pk):
#     blog = get_object_or_404(Blog, pk=pk)
#     context = {
#         'blog': blog
#     }
#     return render(request, 'blog_details.html', context)



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_details.html'  # Template yolu
    context_object_name = 'blog' 
