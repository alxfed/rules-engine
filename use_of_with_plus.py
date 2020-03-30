# -*- coding: utf-8 -*-
"""https://docs.python.org/3/reference/compound_stmts.html#with
"""


class ContextManager(object):

    def __init__(self, name:str):

        print('defining context name:', name)
        self.name = name

    def __enter__(self):

        try:
            print('Enter, appended to stack:', self.name)
        except:
            raise Exception('could not enter the context')
        finally:
            print('defined context name:', self.name)

        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        print('now exiting')
        return exc_value


def main():
    with ContextManager('context name') as exit_value:
        print(exit_value)

    print('after with')
    return


if __name__ == '__main__':
    main()
    print('\ndone')