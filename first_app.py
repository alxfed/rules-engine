# -*- coding: utf-8 -*-
"""https://github.com/jruizgit/rules/blob/master/docs/py/reference.md
"""
from durable.lang import *


def main():

    with ruleset('test'):
        @when_any(m.subject == 'World')
        def say_hello(c):
            print(f'Hello {c.m.subject}')

    post('test', {'subject': 'World'})
    return


if __name__ == '__main__':
    main()
    print('\ndone')