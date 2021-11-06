from django.shortcuts import render
# Create your views here.

posts = [
    {
        'driver': 'JonathanR',
        'title' : 'Miles Driven',
        'miles': '136',
        'date_driven': 'October 27 2021'
    },
    {
        'driver': 'JonathanR',
        'title' : 'Miles Driven',
        'miles': '143',
        'date_driven': 'October 28 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'milage/home.html', context, )

def about(request):
    return render(request,'milage/about.html', {'title': 'About'})
