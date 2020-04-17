# coding=utf-8


class Pizza:
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.cheese = builder.cheese

    def __str__(self):
        return 'garlic: {}, cheese: {}'.format(self.garlic, self.cheese)


class PizzaBuilder:
    def __init__(self):
        self.garlic = False
        self.cheese = False

    def add_garlic(self):
        self.garlic = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def build(self):
        return Pizza(self)


if __name__ == '__main__':
    pizza = PizzaBuilder().add_garlic().add_cheese().build()
    print pizza
