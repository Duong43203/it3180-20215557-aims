from dvd import DigitalVideoDisc

class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc: DigitalVideoDisc) -> bool:
        # Lỗi cố ý off-by-one: > thay vì >= (sẽ sửa ở Lab 03)
        if len(self.items) > self.MAX_NUMBERS_ORDERED:
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
