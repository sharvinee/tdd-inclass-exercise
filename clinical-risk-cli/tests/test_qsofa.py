import unittest
from clinical_risk.risk_scores import qsofa_score


class TestQSOFA(unittest.TestCase):

    def test_all_criteria_met(self):
        # TODO: Write a test case where all criteria are met and the score is 3.
        self.assertEqual(qsofa_score(23, 90, True), 3)
        

    def test_no_criteria_met(self):
        #TODO: Write a test case where no criteria are met and the score is 0.
        self.assertEqual(qsofa_score(18, 120, False), 0)

    def test_partial_criteria(self):
        # TODO: Write a test case for partial criteria met.
        self.assertEqual(qsofa_score(19, 99, True), 2)
        self.assertEqual(qsofa_score(22, 120, False), 1)
        self.assertEqual(qsofa_score(18, 90, False), 1)
        self.assertEqual(qsofa_score(18, 120, True), 1)


    def test_invalid_rr_raises(self):
        # TODO: Write a test case that checks if an invalid respiratory rate raises an error.
        # Hint: You can use self.assertRaises to check for exceptions.
        self.assertRaises(ValueError, qsofa_score(-1, -1, False))