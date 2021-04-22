from django.shortcuts import render

def todoList(request):
    return render(request, 'todopage/index.html')