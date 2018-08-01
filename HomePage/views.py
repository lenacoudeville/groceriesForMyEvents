from django.shortcuts import render

# Create your views here.
def HomePage(request):
	template = 'HomePage/HomePage.html'
	return render(request, template, {})