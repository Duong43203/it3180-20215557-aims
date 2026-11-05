import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", "Category", "Director", 90, 10.0)
            self.assertTrue(cart.add_digital_video_disc(dvd))
        
        # Đĩa thứ 21 phải trả về False do giới hạn giỏ hàng tối đa 20
        dvd_21 = DigitalVideoDisc("DVD 21", "Category", "Director", 90, 10.0)
        self.assertFalse(cart.add_digital_video_disc(dvd_21))

    def test_total_cost(self):
        cart = Cart()
        cart.add_digital_video_disc(DigitalVideoDisc("DVD 1", cost=19.95))
        cart.add_digital_video_disc(DigitalVideoDisc("DVD 2", cost=24.95))
        cart.add_digital_video_disc(DigitalVideoDisc("DVD 3", cost=18.99))
        self.assertAlmostEqual(cart.total_cost(), 63.89, places=2)

    def test_discount_valid(self):
        cart = Cart()
        cart.add_digital_video_disc(DigitalVideoDisc("DVD 1", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0, places=2)

    def test_discount_invalid(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Star Wars", cost=20)
        d2 = DigitalVideoDisc("Aladin", cost=15)
        cart.add_digital_video_disc(d1)
        cart.add_digital_video_disc(d2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladin")

    def test_sort_by_cost(self):
        cart = Cart()
        d1 = DigitalVideoDisc("DVD Cheap", cost=10)
        d2 = DigitalVideoDisc("DVD Expensive", cost=50)
        cart.add_digital_video_disc(d1)
        cart.add_digital_video_disc(d2)
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 50)

if __name__ == "__main__":
    unittest.main()
