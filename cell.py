
class Cell:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords
        
    def is_solved(self):
        return self.value != 0
