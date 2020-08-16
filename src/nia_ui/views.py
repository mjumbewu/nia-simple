from django.shortcuts import render

def board(request):
    return render(request, 'nia_ui/board.html')