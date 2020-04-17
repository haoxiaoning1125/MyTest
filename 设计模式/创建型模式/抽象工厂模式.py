# coding=utf-8


class Frog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print '{} the frog encounters {} and {}!'.format(
            self, obstacle, obstacle.action()
        )


class Bug(object):
    def __str__(self):
        return 'a bug'

    @staticmethod
    def action():
        return 'eats it'


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print '{} the Wizard battles against {} and {}!'.format(
            self, obstacle, obstacle.action()
        )


class Ork(object):
    def __str__(self):
        return 'an evil ork'

    @staticmethod
    def action():
        return 'kills it'


class FrogWorld(object):
    def __init__(self, player_name):
        self.player_name = player_name

    def __str__(self):
        return '\n\n\t------------ Frog World -------------'

    def make_character(self):
        return Frog(self.player_name)

    @staticmethod
    def make_obstacle():
        return Bug()


class WizardWorld(object):
    def __init__(self, player_name):
        self.player_name = player_name

    def __str__(self):
        return '\n\n\t----------- Wizard World ------------'

    def make_character(self):
        return Wizard(self.player_name)

    @staticmethod
    def make_obstacle():
        return Ork()


class GameEnvironment(object):
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = raw_input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as ve:
        print 'Age {} is invalid, please try again.'.format(age)
        return False, age
    return True, age


def main():
    name = raw_input('Input your name: ')
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
