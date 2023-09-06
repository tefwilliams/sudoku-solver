class Cell:
    was_changed = False

    def __init__(self, value: int | None):
        self.value = value
        self.__potential_values = [] if value else [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def is_solved(self) -> bool:
        return self.value is not None

    def has_no_potential_values(self) -> bool:
        return len(self.__potential_values) == 0

    def set_value(self, value: int) -> None:
        self.__potential_values.remove(value)
        self.value = value

    def is_wrong(self):
        is_wrong = (not self.is_solved() and self.has_no_potential_values()) or (
            self.is_solved() and not grid.possible(self.coords, self.value)
        )

        if is_wrong:
            print(self.value, self.coords)

        return is_wrong
