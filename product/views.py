from django.views.generic import DetailView, ListView
from .models import Product, Category
from django.shortcuts import get_object_or_404


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 1

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        categories = category.get_descendants(include_self=True)
        qs = super(ProductList, self).get_queryset().filter(category__in=categories)
        return qs
