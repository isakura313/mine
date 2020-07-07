from index import Enemy
from Hero import Hero

steve = Hero("Steve", 20, 10, 0, 10)
while True:
    time = input("Какое сейчас время?")
    if time == 'day':
        print("Здорово")
    if time == 'night':
        slizen = Enemy("чмонк чмонк", 50, 10, 5, 10)
        slizen.sound()
        zombi = Enemy("УУУУУУэээ", 70, 20, 2, 10)
        zombi.sound()
        steve.take_damage(zombi.damage)
        print(steve.hp)


