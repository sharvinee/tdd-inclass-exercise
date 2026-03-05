import unittest
from clinical_risk.risk_scores import qsofa_score


class TestQSOFA(unittest.TestCase):

    def test_all_criteria_met(self):
        # TODO: Write a test case where all criteria are met and the score is 3.
        pass
        

    def test_no_criteria_met(self):
        #TODO: Write a test case where no criteria are met and the score is 0.
        pass

    def test_partial_criteria(self):
        # TODO: Write a test case for partial criteria met.
        pass

    def test_invalid_rr_raises(self):
        # TODO: Write a test case that checks if an invalid respiratory rate raises an error.
        # Hint: You can use self.assertRaises to check for exceptions.
        pass