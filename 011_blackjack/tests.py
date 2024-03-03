import unittest
from main import deal_card, calculate_score, compare_scores


class TestBlackjackFunctions(unittest.TestCase):
    def test_deal_card(self):
        """Test if the deal_card function provides valid card values"""
        card = deal_card()
        self.assertIn(card, [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_calculate_score(self):
        """Test various card combinations in the calculate_score function"""
        # Testing Blackjack
        self.assertEqual(calculate_score([11, 10]), 0)

        # Testing Aces
        # Here the Ace should become 1 as the total would go above 21
        self.assertEqual(calculate_score([11, 10, 2]), 13)
        # Here Ace remains 11
        self.assertEqual(calculate_score([11, 7]), 18)

        # Testing other cards
        self.assertEqual(calculate_score([10, 4]), 14)
        self.assertEqual(calculate_score([5, 2]), 7)

    def test_compare_scores(self):
        """Test different scenarios in compare_scores function"""
        # Testing both with Blackjack
        self.assertEqual(compare_scores(0, 0), "It's a Draw! Both have a Blackjack!")

        # Testing dealer with Blackjack
        self.assertEqual(compare_scores(20, 0), "You lose, the dealer has a Blackjack")

        # Testing user with Blackjack
        self.assertEqual(compare_scores(0, 20), "You win!! with a Blackjack")

        # Testing draws without Blackjack
        self.assertEqual(compare_scores(20, 20), "It's a Draw!")

        # Testing user going over 21
        self.assertEqual(compare_scores(22, 20), "You lose, you went over")

        # Testing dealer going over 21
        self.assertEqual(compare_scores(20, 22), "You win! the dealer went over")

        # Testing user wins by having a greater score than dealer
        self.assertEqual(compare_scores(20, 18), "You win!")

        # Testing dealer wins by having a greater score than user
        self.assertEqual(compare_scores(18, 20), "You lose")


if __name__ == "__main__":
    unittest.main()
