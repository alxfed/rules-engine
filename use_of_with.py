# -*- coding: utf-8 -*-
"""https://docs.python.org/3/reference/compound_stmts.html#with
"""
stack = []


class ContManager(object):

    def __init__(self, name:str):
        self.rules = []
        self.name = name

    def __enter__(self):
        try:
            stack.append(self)
            print('Enter, appended to stack:', self.name)
        except:
            raise Exception('could not enter the context')
        finally:
            print('defined context name:', self.name)
            print(stack)

    def __exit__(self, exc_type, exc_value, traceback):
        stack.pop()
        print('Poped from the stack, now exiting')
        print(stack)

    def define(self): # ??
        index = 0
        new_definition = {}
        for rule in self.rules:
            new_definition[f'r_{index}'] = rule.define()
            index += 1
        return self.name, new_definition


if __name__ == '__main__':
    with ContManager('context name'):
        print('ending with')

    print('this is after with')


'''
Also: https://docs.python.org/3/library/contextlib.html#contextlib.ContManager
and https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
'''
