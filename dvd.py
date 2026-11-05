class DigitalVideoDisc:
    def __init__(self, title: str, category: str = "", director: str = "", length: int = 0, cost: float = 0.0):
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = cost

    def __repr__(self):
        return f"DVD({self.title}, {self.category}, {self.director}, {self.length}, {self.cost})"
