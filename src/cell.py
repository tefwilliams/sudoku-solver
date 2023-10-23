from helpers import allowed_values


class Cell:
    def __init__(self, value: int | None):
        assert value is None or value in allowed_values
        self.__value = value
        # TODO - Maybe use set
        self.potential_values = set([] if value else allowed_values)

    @property
    def is_solved(self) -> bool:
        return self.__value is not None
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        self.potential_values.remove(value)
        self.__value = value

    def has_no_possible_value(self):
        return not self.is_solved and len(self.potential_values) == 0
