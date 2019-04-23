from django.shortcuts import render
from .models import Review 


def home(request):
	return render(request,'reviewApp/home.html', {'title':'Home'})

def contact(request):
	return render(request, 'reviewApp/contact.html', {'title':'Contact'})

def about(request):
	return render(request, 'reviewApp/about.html', {'title':'About'} )

## def reviews(request):
	## return render(request, 'reviewApp/reviews.html')

def report(request):
	daily_report={
	'review': Review.objects.all()
	}
	return render(request, 'reviewApp/report.html', {'title':'Review'}, daily_report)

def product(request):
	return render(request, 'reviewApp/product.html', {'title':'Products'})

# Create your views here.
