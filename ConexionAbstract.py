# -*- coding: utf-8 -*-

"""
 Clase abstracta para implementar un CRUD en Python
 @author Jess
 @version 1.0
"""
from abc import ABC, abstractmethod

class ConexionAbstract(ABC):
    @abstractmethod
    def create():
        pass
    @abstractmethod
    def read():
        pass
    @abstractmethod
    def update():
        pass
    @abstractmethod
    def delete():
        pass
    @abstractmethod
    def insert():
        pass
    