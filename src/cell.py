from helpers import allowed_values


class Cell:
    def __init__(self, value: int | None):
        # TODO - should allowed values be a type?
        assert value is None or value in allowed_values
        self.__value = value
        self.possible_values = set([] if value else allowed_values)
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        self.possible_values.clear()
        self.__value = value
