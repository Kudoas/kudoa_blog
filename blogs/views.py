from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Category


class IndexView(generic.ListView):
    model = Post
    paginate_by = 3
    template_name = 'blogs/post_list.html'

    def get_queryset(self):
        queryset = Post.objects.order_by('-pub_date')
        keyword = self.request.GET.get('keyword')

        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )

        return queryset


class CategoryView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-pub_date').filter(category=category)
        return queryset


class DetailView(generic.DetailView):
    model = Post


class IntroView(generic.TemplateView):
    template_name = 'blogs/intro.html'
