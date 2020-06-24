from django.views.generic import CreateView, UpdateView, ListView
from django.utils.text import slugify
from product.models import Brand


class BrandCreate(CreateView):
    model = Brand
    template_name = 'dashboard/brand/create.html'
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + '-' + str(instance.id)
        instance.save()
        return super(BrandCreate, self).form_valid(form)


class BrandUpdate(UpdateView):
    model = Brand
    template_name = 'dashboard/brand/create.html'
    fields = ['name', 'image']

    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + '-' + str(instance.id)
        instance.save()
        return super(BrandUpdate, self).form_valid(form)


class BrandList(ListView):
    model = Brand
    template_name = 'dashboard/brand/list.html'