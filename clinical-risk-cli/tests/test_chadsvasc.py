import unittest
from clinical_risk.risk_scores import cha2ds2_vasc_score


class TestCHADS2VASc(unittest.TestCase):

    def test_age_over_75(self):
        # TODO: Write a test case for age over 75, which should contribute 2 points to the score.
        pass

    def test_multiple_risk_factors(self):
        # TODO: Write a test case for multiple risk factors, such as age 65-74, female sex, and hypertension, which should contribute a total of 3 points to the score.
        pass

    def test_no_risk_factors(self):
        # TODO: Write a test case for no risk factors, which should result in a score of 0.
        pass

    # TODO: write your own test cases for the CHA2DS2-VASc score here. Consider edge cases and combinations of risk factors.