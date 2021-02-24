class Minimum:
    def __init__(self, initial_value):
        self.value = initial_value

    def update_minimum(self, potential_min):
        if potential_min < self.value:
            self.value = potential_min
