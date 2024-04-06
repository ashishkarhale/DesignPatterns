from abc import ABC , abstractmethod

#Product
class Sandwich:
    def __init__(self):
        self.sauces = []
        self.bread_type = 'Whole Wheat'
        self.vegetables = []
        self.size = 'Small'

    def __str__(self) -> str:
        return f"{self.bread_type} {self.size} sandwhich with sauces {','.join(self.sauces)} \
            and with vegetables as {','.join(self.vegetables)}"
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

#concrete builder
class SandwichBuilder(SandwichBuilderInterface):
    def __init__(self):
        self.sandwhich = Sandwich()
    def add_sauses(self,sauce):
        return self.sandwhich.sauces.append(sauce)
    def bread_type(self,bread_type):
        self.sandwhich.bread_type = bread_type
        return self
    def add_vegetables(self,vegetable):
        return self.sandwhich.vegetables.append(vegetable)
    def specify_size(self,size):
        self.sandwhich.size = size
        return self
    def build(self):
        return self.sandwhich

#direcector
class SandwhichDirector:
    def construct(self,sauces , bread_type , vegetables , size):
        sandwhich_builder = SandwichBuilder()
        for sauce in sauces:
            sandwhich_builder.add_sauses(sauce)
        for vegetable in vegetables:
            sandwhich_builder.add_vegetables(vegetable)
        sandwhich_builder.bread_type(bread_type)
        sandwhich_builder.specify_size(size)
        return sandwhich_builder.build()

#Client
sandwhich = SandwhichDirector().construct(['red','white'],'Gluten Free',['onion','cabbage'],'Large')

print(sandwhich)