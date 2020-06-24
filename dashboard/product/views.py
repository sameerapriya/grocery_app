from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView
from product.models import Product


class ProductCreate(CreateView):
    model = Product
    template_name = 'dashboard/product/create.html'
    fields = ['name', 'description', 'price', 'weight', 'sku', 'stock', 'brand', 'category']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + '-' + str(instance.id)
        instance.save()
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'dashboard/product/create.html'
    fields = ['name', 'description', 'price', 'weight', 'sku', 'stock', 'brand', 'category']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + '-' + str(instance.id)
        instance.save()
        return super(ProductUpdate, self).form_valid(form)


class ProductList(ListView):
    model = Product
    template_name = 'dashboard/product/list.html'
