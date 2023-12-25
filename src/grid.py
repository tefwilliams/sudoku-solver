import numpy as np
from helpers import null_value, is_wrong, allowed_values


class Grid:
    def __init__(self, values: np.ndarray):
        # TODO - Assert all values allowed
        self.values = values
        self.guesses: dict[tuple[int, int], set[int]] = {}

    @property
    def is_solved(self):
        return all(
            cell != null_value
            for cell
            in self.values.flatten()
        )

    @property
    def is_wrong(self):
        return any(
            is_wrong(self.values[*get_row(i)].flatten()) or
            is_wrong(self.values[*get_col(i)].flatten()) or
            is_wrong(self.values[
                *get_square((i // 3) * 3, (i % 3) * 3)
            ].flatten())
            for i in range(9)
        )

    def get_single_possible_value(self, row: int, col: int):
        possible_values = self.get_possible_values(row, col)

        if len(possible_values) == 1:
            return possible_values.pop()

        return null_value

    def get_unique_possible_value(self, row: int, col: int):
        '''
        Check if any value is only possible for one cell
        '''

        return (self.get_unique_poss(get_row(row), row, col)
                or self.get_unique_poss(get_col(col), row, col)
                or self.get_unique_poss(get_square(row, col), row, col))

    def get_unique_poss(self, mgrid: np.ndarray, row: int, col: int):
        y_coords, x_coords = mgrid

        # Get the coordinates of all cells
        # except the current cell
        cells = np.array([
            cell for cell
            in np.vstack([y_coords.ravel(), x_coords.ravel()]).T
            if not (cell[0] == row and cell[1] == col)
        ])

        # Get all values that are 'possible'
        # for other cells
        values_possible_for_other_cells = set().union(
            *(
                self.get_possible_values(*cell)
                for cell in cells
            )
        )

        values_only_possible_for_current_cell = set(
            value for value
            in self.get_possible_values(row, col)
            if value not in values_possible_for_other_cells
        )

        if len(values_only_possible_for_current_cell) > 1:
            raise ValueError("Multiple values are only possible for one cell")

        if len(values_only_possible_for_current_cell) == 1:
            return values_only_possible_for_current_cell.pop()

        return null_value

    def get_possible_values(self, row: int, col: int) -> set[int]:
        if self.values[row, col] is null_value:
            return set()

        disallowed_values = set().union(
            self.values[*get_row(row)].flatten(),
            self.values[*get_col(col)].flatten(),
            self.values[*get_square(row, col)].flatten(),
            self.guesses.get((row, col)) or set()
        )

        return set(
            value
            for value in allowed_values
            if value not in disallowed_values
        )

    def __str__(self):
        return "\n".join(
            f"""\
{row[0:3]}  \
{row[3:6]}  \
{row[6:9]}  \
{"\n" if i in [2, 5] else ""}\
"""
            .replace(",", "")
            .replace(f"{null_value}", "-")
            .replace("[", "")
            .replace("]", "")
            for i, row in enumerate(self.values)
        )


def get_row(row: int):
    return np.mgrid[row: row + 1, 0: 9]


def get_col(col: int):
    return np.mgrid[0: 9, col: col + 1]


def get_square(row: int, col: int):
    min_row = (row // 3) * 3
    min_col = (col // 3) * 3

    return np.mgrid[min_row: min_row + 3, min_col: min_col + 3]
