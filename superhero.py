
class OrdinaryMan():

    def __init__(self, name):

        self.name = name

    def reveal_name(self):

        print(f'My name is {self.name}')

class SuperHero(OrdinaryMan):

    def __init__(self, name, heroname):
        self.heroname = heroname
        super().__init__(name)

    def reveal_name(self):

        super().reveal_name()

        print(f'... and I am also {self.heroname}')

    def make_sound(self):
        name = self.heroname
        print(f'{name*3}')


if __name__ == "__main__":
    ord = SuperHero("Onder", "CodeMan")
    ord.reveal_name()
    ord.make_sound()

    print(f'normal: {ord.name} hero: {ord.heroname}')
