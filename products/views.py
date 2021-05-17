from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView

from comments.models import Comment
from products.forms import ProductForm
from products.models import Product


class ProductsListView(ListView):

    template_name = "product_list.html"
    model = Product
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-updated')


class ProductDetailView(DetailView):
    template_name = "product_details.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.filter(id=kwargs['object'].pk)
        context['product'] = product.first()
        if Comment.objects.filter(product=product.exists()):
            context['comments'] = Comment.objects.filter(product=product.first()).order_by('-created')
            print('comments', context['comments'])
        return context


class ProductUserView(View):

    def get(self, request, *args, **kwargs):
        print('here', request.user)
        if request.user.is_authenticated:
            products_user = Product.objects.filter(author=request.user)
            print('data:', products_user)
            return render(request, 'product_user.html', context={'products': products_user})
        return redirect('/')

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, instance=request.user)
        print('test1', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
        return render(request, 'product_update.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['image', 'name', 'description', 'price']
    template_name = 'product_update.html'
    success_url = '/profile'


class SearchProductView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('search_box')
        if query:
            object_list = Product.objects.filter(
                Q(name__icontains=query) | Q(author__username__icontains=query)
            )
            return object_list
        return Product.objects.all()
