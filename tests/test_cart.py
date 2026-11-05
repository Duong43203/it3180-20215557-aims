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

if __name__ == "__main__":
    unittest.main()
