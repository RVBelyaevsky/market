from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, ContactTemplateView, BlogCreateView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, BlogListView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('product/<int:pk>/', cache_page(60)(CatalogDetailView.as_view()), name='product'),
    path('create/', CatalogCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>', CatalogUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>', CatalogDeleteView.as_view(), name='product_delete'),

    path('contacts/', ContactTemplateView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
