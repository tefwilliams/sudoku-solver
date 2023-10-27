from helpers import allowed_values


class Cell:
    def __init__(self, value: int | None):
        assert value is None or value in allowed_values
        self.__value = value
        # TODO - Maybe use set
        self.possible_values = set([] if value else allowed_values)
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        self.possible_values.clear()
        self.__value = value

    # Yuck
    def has_no_possible_value(self):
        return not self.value and len(self.possible_values) == 0
