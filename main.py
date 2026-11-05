from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

def main():
    print("=== AIMS-mini v1.0.0 ===")
    cart = Cart()
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95)
    dvd3 = DigitalVideoDisc("Aladin", "Animation", "John Musker", 90, 18.99)

    cart.add_digital_video_disc(dvd1)
    cart.add_digital_video_disc(dvd2)
    cart.add_digital_video_disc(dvd3)

    cart.print_cart()

if __name__ == "__main__":
    main()
