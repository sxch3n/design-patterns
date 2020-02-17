from abc import ABCMeta, abstractmethod

# TODO: define a cached instance for unique instance reference callback
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p25_creating_cached_instances.html
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
