class Node:
    def __init__(self, name):
        self.neighbours = {}
        self.name = name

    def print(self):
        for neighbour in self.neighbours.keys():
            print(f"Current node: {self.name}")
            print(f"To: {neighbour} - distance: {self.neighbours[neighbour]}")
