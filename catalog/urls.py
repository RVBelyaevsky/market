from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, ContactTemplateView, BlogCreateView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, BlogListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', CatalogDetailView.as_view(), name='product'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
