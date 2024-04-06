from django.shortcuts import render

# Create your views here.


task_posts = [
    {
        'task_category' :  'SOCIAL',
        'task_date': '6th March 2024',
        'task_context' : 'This is just for educational purposes'
    },
    {
        'task_category' :  'COORPORATE',
        'task_date': '7th March 2024',
        'task_context' : 'This is just for  purposes'
    }
]

def home(request):
    context = {
        'task' : task_posts
    }
    
    return render(request, 'index.html', context)
