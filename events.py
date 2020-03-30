# -*- coding: utf-8 -*-
"""...
"""
from durable.lang import *


def main():
    with ruleset('risk'):
        @when_all(c.first << m.t == 'purchase',
                  c.second << m.location != c.first.location)
        # the event pair will only be observed once
        def fraud(c):
            print('Fraud detected -> {0}, {1}'.format(c.first.location, c.second.location))

    post('risk', {'t': 'purchase', 'location': 'US'})
    post('risk', {'t': 'purchase', 'location': 'CA'})
    return


if __name__ == '__main__':
    main()
    print('\ndone')