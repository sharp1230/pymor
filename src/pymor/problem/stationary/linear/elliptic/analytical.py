#!/usr/bin/env python

from __future__ import print_function

from pymor.core import BaseInterface
from pymor.common import function


class Interface(BaseInterface):

    def name(self):
        return 'problem.stationary.linear.elliptic'

    @BaseInterface.abstractmethod
    def diffusion(self):
        pass

    @BaseInterface.abstractmethod
    def force(self):
        pass

    @BaseInterface.abstractmethod
    def dirichlet(self):
        pass

    @BaseInterface.abstractmethod
    def neumann(self):
        pass


class Default(Interface):

    def __init__(self, name='problem.stationary.linear.elliptic.default'):
        self._name = name
        self._diffusion = function.nonparametric.Constant(1, 'diffusion')
        self._force = function.nonparametric.Constant(1, 'force')
        self._dirichlet = function.nonparametric.Constant(0, 'dirichlet')
        self._neumann = function.nonparametric.Constant(0, 'neumann')

    def name(self):
        return self._name

    def diffusion(self):
        return self._diffusion

    def force(self):
        return self._force

    def dirichlet(self):
        return self._dirichlet

    def neumann(self):
        return self._neumann


if __name__ == "__main__":
    print('creating problem... ', end='')
    p = Default()
    print('done (' + p.name() + ')')