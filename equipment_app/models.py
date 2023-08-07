from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.number

class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('smartphone', 'Smartphone'),
        ('tablet', 'Tablette'),
        ('screen', 'Écran'),
        ('projector', 'Vidéo-Projecteur'),
        ('laser_pointer', 'Pointeur Laser'),
    ]
    BUDGET_CHOICES = [
        ('current_year', 'Current Year Budget'),
        ('projects', 'Projects Budget'),
        ('exceptional', 'Exceptional Financing'),
        # add other budget options here
    ]
    type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, default='current_year')
    accessories = models.TextField()
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    current_location = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='location', default=1)
    current_possessor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='possessor')

    def __str__(self):
        return self.type


class Transfer(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    from_possessor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='from_possessor')
    to_possessor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='to_possessor')
    date = models.DateTimeField()
    location = models.ForeignKey(Room, on_delete=models.CASCADE)
    occasion = models.CharField(max_length=100)
    accessories_state = models.TextField()

    def __str__(self):
        return f'{self.equipment} transfer from {self.from_possessor} to {self.to_possessor}'

