from django.shortcuts import render

reviews = [
{
'author' : 'Emma Cook',
'rating' : '4 stars',
'review' : 'fantastic product, would recommend',
'date' : '19/04/2019'
}
]

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
	'reviews': reviews
	}
	return render(request, 'reviewApp/report.html', {'title':'Report'}, daily_report)


# Create your views here.
