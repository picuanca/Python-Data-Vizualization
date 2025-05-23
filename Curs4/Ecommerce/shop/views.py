from django.shortcuts import render, redirect



# Create your views here.
from .models import Product, Category

def all_products_view(request):

	products = Product.objects.all()

	context = {
		"products": products
	}

	return render(request, 'all_products.html', context)

def product_details_view(request):
	context = {}
	return render(request, 'product_details.html', context)

def all_categories_view(request):
	categories = Category.objects.all()

	context = {
		"categories": categories
	}
	return render(request, 'all_categories.html', context)

def category_details_view(request, slug):
	category_details = Category.objects.filter(slug=slug).first()
	if not category_details:
		return redirect("categories_url")
	
	products = Product.objects.filter(category=category_details)

	context = {"category": category_details,
			"products": products
			}

	return render(request, 'category_details.html', context)
