from aims.dvd import DigitalVideoDisc

class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc: DigitalVideoDisc) -> bool:
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            return False
        self.items.append(disc)
        print(f"The disc '{disc.title}' has been added")
        return True

    def remove_digital_video_disc(self, disc: DigitalVideoDisc) -> bool:
        if disc in self.items:
            self.items.remove(disc)
            return True
        return False

    def total_cost(self) -> float:
        return sum(item.cost for item in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
