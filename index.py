class Enemy:
    def __init__(self, name, hp, speed, armor, damage):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.armor = armor
        self.damage = damage
    def sound(self):
        print(f"{self.name}")
    def attack(self, igrock):
        igrock.hp - self.damage
