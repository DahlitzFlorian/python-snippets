from abc import ABCMeta, abstractmethod


class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class ConcreteClass(BaseClass):
    def foo(self):
        pass

    def bar(self):
        pass


instance = ConcreteClass()
