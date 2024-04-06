from abc import ABC , abstractmethod

#builder interface
class SandwichBuilderInterface(ABC):
    @abstractmethod
    def add_sauses(self):
        pass

    @abstractmethod
    def bread_type(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def specify_size(self):
        pass



