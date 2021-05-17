from django.urls import path

from products.views import ProductsListView, ProductDetailView, ProductUserView, ProductUpdateView, SearchProductView

urlpatterns = [
    path('', ProductsListView.as_view()),
    path('product/create/', ProductsListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),

    path('profile/', ProductUserView.as_view(), name='user_products'),
    path('profile/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('search/', SearchProductView.as_view(),  name='search_products')
]
