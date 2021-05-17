from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from products.models import Product


def add_comment_to_post(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect(f'/product/{product.pk}')
    else:
        form = CommentForm()
    return render(request, 'comment_create.html', {'form': form})
