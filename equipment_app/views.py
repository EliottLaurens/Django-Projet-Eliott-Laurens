from django.shortcuts import render, redirect
from .models import Teacher, Room, Equipment, Transfer

def index(request):
    return render(request, 'index.html')

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST['name']
        Teacher.objects.create(name=name)
        return redirect('teachers')
    return render(request, 'add_teacher.html')

def teacher_responsibility(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    equipment_responsible = Equipment.objects.filter(owner=teacher)
    return render(request, 'teacher_responsibility.html', {'teacher': teacher, 'equipment_responsible': equipment_responsible})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def add_room(request):
    if request.method == "POST":
        room_number = request.POST['room_number']
        Room.objects.create(room_number=room_number)
        return redirect('rooms')
    return render(request, 'add_room.html')

def equipment_in_room(request, room_id):
    room = Room.objects.get(id=room_id)
    equipment_in_room = Equipment.objects.filter(current_location=room)
    return render(request, 'equipment_in_room.html', {'room': room, 'equipment_in_room': equipment_in_room})

def equipment_transfers(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    transfers = Transfer.objects.filter(equipment=equipment)
    return render(request, 'equipment_transfers.html', {'equipment': equipment, 'transfers': transfers})



def equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment.html', {'equipments': equipments})


def add_equipment(request):
    teachers = Teacher.objects.all()
    rooms = Room.objects.all()
    if request.method == "POST":
        type = request.POST['type']
        accessories = request.POST['accessories']
        owner_id = request.POST['owner']
        location_id = request.POST['location']
        possessor_id = request.POST['possessor']
        owner = Teacher.objects.get(id=owner_id)
        location = Room.objects.get(id=location_id)
        possessor = Teacher.objects.get(id=possessor_id)
        Equipment.objects.create(type=type, accessories=accessories, owner=owner, current_location=location, current_possessor=possessor)
        return redirect('equipment')
    return render(request, 'add_equipment.html', {'teachers': teachers, 'rooms': rooms})

def transfers(request):
    transfers = Transfer.objects.all()
    return render(request, 'transfers.html', {'transfers': transfers})

def transfer_equipment(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    teachers = Teacher.objects.exclude(id=equipment.current_possessor.id)
    rooms = Room.objects.all()
    if request.method == "POST":
        to_possessor_id = request.POST['to_possessor']
        date = request.POST['date']
        location_id = request.POST['location']
        occasion = request.POST['occasion']
        accessories_state = request.POST['accessories_state']
        to_possessor = Teacher.objects.get(id=to_possessor_id)
        location = Room.objects.get(id=location_id)
        Transfer.objects.create(equipment=equipment, from_possessor=equipment.current_possessor, to_possessor=to_possessor, date=date, location=location, occasion=occasion, accessories_state=accessories_state)
        equipment.current_possessor = to_possessor
        equipment.current_location = location
        equipment.save()
        return redirect('transfers')
    return render(request, 'transfer_equipment.html', {'equipment': equipment, 'teachers': teachers, 'rooms': rooms})
