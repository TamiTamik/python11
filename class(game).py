import random
class hero:
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('Hi, I am Hero', self.name, ',I have', self.hp, 'hp', 'and', self.damage,'damage')
    def hit(self) -> int:
        return self.damage

    def attack(self, damage: int) -> bool:
        if self.hp - damage <= 0:
            print(self.name, 'sdoh...')
            return True
        else:
            self.hp = self.hp - damage
            return False

you = hero('Tamir', 120, 30)
monster = hero('Tulga', 110, 20)

while True:
    lucky = random.randrange(1,5)
    too = int(input('Guess which from 1 to 4: '))
    if lucky == too:
        print('ebash')
        dead = monster.attack(you.hit())
        print('hp monstra:', monster.hp)
    else:
        print('poluchai')
        dead = you.attack(monster.hit())
        print('tvoi hp:', you.hp)

    if dead:
        break
else:
    print('Game over...')

