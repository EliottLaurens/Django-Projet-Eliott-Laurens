from django.shortcuts import render
from .models import Teacher, Room, Equipment, Transfer

def index(request):
    return render(request, 'index.html')

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment.html', {'equipment': equipment})

def transfers(request):
    transfers = Transfer.objects.all()
    return render(request, 'transfers.html', {'transfers': transfers})
