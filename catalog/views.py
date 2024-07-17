from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, BlogForm
from catalog.models import Product, Blog


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User:{name}(phone number:{phone}) send message: "{message}"')

        return render(request, 'catalog/contacts.html')


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content',)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
