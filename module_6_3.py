import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]

    def __init__(self, speed: int):
        super().__init__()
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        cords = [self.dx, self.dy, self.dz]
        self._cords = [i * self.speed for i in cords]
        if self._cords[2] < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            return self._cords

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print('Here are(is)', random.randint(0, 5), 'eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz)*self.speed*.5
        self._cords[2] = round(new_z)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = 'Click-click-click'

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()