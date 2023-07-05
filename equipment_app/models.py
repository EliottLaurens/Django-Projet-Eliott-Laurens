from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    number = models.CharField(max_length=10)

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    accessories = models.CharField(max_length=200)
    buyer = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="equipment_bought")
    owner = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="equipment_owned")
    current_holder = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="equipment_held")
    current_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

class Transfer(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    old_holder = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="transfers_out")
    new_holder = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="transfers_in")
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(max_length=200)
