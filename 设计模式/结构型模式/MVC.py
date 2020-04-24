# coding=utf-8
# 模型-视图-控制器模式

import random


class QuotesModel(object):
    quotes = (
        'A man is not complete until he is married. Then he is finished.',
        'As I said before, I never repeat myself.',
        'Behind a successful man is an exhausted woman.',
        'Black holes really suck...',
        'Facts are stubborn things.',
    )

    def get_quotes(self, index):
        try:
            ret = self.__class__.quotes[index]
        except IndexError:
            ret = 'Not found.'
        return ret

    def get_random_quotes(self):
        return random.choice(self.__class__.quotes)


class QuotesTerminalView(object):
    @staticmethod
    def show(quote):
        print 'Quote is {}'.format(quote)

    @staticmethod
    def error(msg):
        print 'Error: {}'.format(msg)

    @staticmethod
    def select_quote():
        return raw_input('Which quote number would you like to see?')


class QuotesTerminalController(object):
    def __init__(self):
        self.model = QuotesModel()
        self.view = QuotesTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                if n == 'random':
                    quote = self.model.get_random_quotes()
                else:
                    n = int(n)
                    quote = self.model.get_quotes(n)
            except ValueError:
                self.view.error('Incorrect index {}'.format(n))
            else:
                valid_input = True
        self.view.show(quote)


if __name__ == '__main__':
    controller = QuotesTerminalController()
    while True:
        controller.run()
