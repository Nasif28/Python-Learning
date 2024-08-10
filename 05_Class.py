class Game:
    life = 3
    def attack(self):
        print('Ouch')
        self.life -= 1
    def life_check(self):
        if self.life <= 0:
            print('You are dead')
        else:
            print(self.life, 'life left')

Enemy1 = Game()
Enemy2 = Game()

Enemy1.attack()
Enemy1.attack()
Enemy1.attack()
Enemy2.attack()
Enemy1.life_check()
Enemy2.life_check()


class Girl:

    gender = 'Female'

    def __int__(self, name):
        self.name = name

r = Girl('FM')
s = Girl('Mim')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

