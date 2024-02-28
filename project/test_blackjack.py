import unittest
from logic import total

#Тестирование функции подсчета очков
class TestTotalFunction(unittest.TestCase):

    def test_1(self):
        cards = ["3_s", "2_h"]
        result = total(cards)
        self.assertEqual(result, 5)
    
    def test_2(self):
        cards = ["10_d", "9_c", "8_h", "7_s", "K_d"]
        result = total(cards)
        self.assertEqual(result, 44)

    def test_3(self):
        cards = ["10_d", "9_c", "A_h"]
        result = total(cards)
        self.assertEqual(result, 20)

    def test_4(self):
        cards = ["2_d", "3_c", "A_s"]
        result = total(cards)
        self.assertEqual(result, 16)
    
    def test_5(self):
        cards = ["A_c", "A_h"]
        result = total(cards)
        self.assertEqual(result, 12)
    
    def test_6(self):
        cards = ["A_c", "5_h", "A_d"]
        result = total(cards)
        self.assertEqual(result, 17)



if __name__ == "__main__":
    unittest.main()
    

    