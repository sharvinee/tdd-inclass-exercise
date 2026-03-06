import unittest
from clinical_risk.risk_scores import cha2ds2_vasc_score


class TestCHADS2VASc(unittest.TestCase):

    def test_age_over_75(self):
        # TODO: Write a test case for age over 75, which should contribute 2 points to the score.
        self.assertEqual(cha2ds2_vasc_score(76, False, False, False, False, False, False), 2)

    def test_multiple_risk_factors(self):
        # TODO: Write a test case for multiple risk factors, such as age 65-74, female sex, and hypertension, which should contribute a total of 3 points to the score.
        self.assertEqual(cha2ds2_vasc_score(70, True, False, True, False, False, False), 3)

    def test_no_risk_factors(self):
        # TODO: Write a test case for no risk factors, which should result in a score of 0.
        self.assertEqual(cha2ds2_vasc_score(30, False, False, False, False, False, False), 0) 

    # TODO: write your own test cases for the CHA2DS2-VASc score here. Consider edge cases and combinations of risk factors.
        self.assertEqual(cha2ds2_vasc_score(80, True, True, True, True, True, True), 9)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, False, False, False), 1)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, False, True, False), 3)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, False, True, True), 4)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, True, False, False), 2)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, True, True, False), 4)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, False, True, True, True), 5)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, True, False, False, False), 2)
        self.assertEqual(cha2ds2_vasc_score(65, False, False, True, False, False, True), 3)
        self.assertRaises(ValueError, cha2ds2_vasc_score(-1, False, False, True, False, True, False), "age must be a non-negative integer")
        self.assertRaises(ValueError, cha2ds2_vasc_score(65, "female", False, True, False, True, False), "female must be a boolean")