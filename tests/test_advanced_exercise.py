import unittest

from src.exercise.advanced_exercise import FiniteStateAutomata
from tests.test_data.test_sample_data import *


class TestFiniteStateAutomata(unittest.TestCase):

    def test_mod_3_transaction(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        expected_transaction = {('s0', '0'): 's0', ('s0', '1'): 's1',
                                ('s1', '0'): 's2', ('s1', '1'): 's0',
                                ('s2', '0'): 's1', ('s2', '1'): 's2'}
        self.assertEqual(expected_transaction, fsm.get_transition())

    def test_mod_3_transaction_map(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        expected_transaction = {'s0': 0, 's1': 1, 's2': 2}
        self.assertEqual(expected_transaction, fsm.get_transition_map())

    def test_mod_3_fsm_config(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        states = 'Q = (s0, s1, s2)'
        alphabet = 'Σ = (0, 1)'
        initial_state = 'q0 = s0'
        final_states = 'F = (s0, s1, s2)'
        results = 'δ(\'s0\', \'0\') = s0; δ(\'s1\', \'0\') = s2; δ(\'s2\', \'0\') = s1; δ(\'s0\', \'1\') = s1; ' \
                  'δ(\'s1\', \'1\') = s0; δ(\'s2\', \'1\') = s2'

        expected_fsm = "\n".join([states, alphabet, initial_state, final_states, results])
        self.assertEqual(expected_fsm, str(fsm))

    def test_mod_3_calculator_valid_input(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        actual = fsm.mod_calculator("110")
        self.assertEqual(0, actual)

        actual = fsm.mod_calculator("1101")
        self.assertEqual(1, actual)

        actual = fsm.mod_calculator("1110")
        self.assertEqual(2, actual)

        actual = fsm.mod_calculator("1010")
        self.assertEqual(1, actual)

    def test_mod_3_calculator_invalid_str_input(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        actual = fsm.mod_calculator("110a")
        self.assertEqual(None, actual)

    def test_mod_3_calculator_invalid_input_type(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        actual = fsm.mod_calculator(11010)
        self.assertEqual(None, actual)

        actual = fsm.mod_calculator(True)
        self.assertEqual(None, actual)

    def test_mod_3_invalid_input_str_length(self):
        fsm = FiniteStateAutomata(states_3, alphabet_3, initial_state_3, final_states_3, transition_results_3)
        actual = fsm.mod_calculator("101010101010101010101010")
        self.assertEqual(None, actual)

    def test_mod_4_transaction(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        expected_transaction = {('s0', 'a'): 's3', ('s0', 'b'): 's1', ('s0', 'c'): 's3',
                                ('s1', 'a'): 's0', ('s1', 'b'): 's2', ('s1', 'c'): 's1',
                                ('s2', 'a'): 's3', ('s2', 'b'): 's0', ('s2', 'c'): 's0',
                                ('s3', 'a'): 's0', ('s3', 'b'): 's1', ('s3', 'c'): 's3'}
        self.assertEqual(expected_transaction, fsm.get_transition())

    def test_mod_4_transaction_map(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        expected_transaction = {'s0': 0, 's1': 1, 's2': 2, 's3': 3}
        self.assertEqual(expected_transaction, fsm.get_transition_map())

    def test_mod_4_fsm_config(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        state = 'Q = (s0, s1, s2, s3)'
        alphabet = 'Σ = (a, b, c)'
        initial_state = 'q0 = s0'
        final_states = 'F = (s2, s3)'
        results = 'δ(\'s0\', \'a\') = s3; δ(\'s1\', \'a\') = s0; δ(\'s2\', \'a\') = s3; δ(\'s3\', \'a\') = s0; ' \
                  'δ(\'s0\', \'b\') = s1; δ(\'s1\', \'b\') = s2; δ(\'s2\', \'b\') = s0; δ(\'s3\', \'b\') = s1; ' \
                  'δ(\'s0\', \'c\') = s3; δ(\'s1\', \'c\') = s1; δ(\'s2\', \'c\') = s0; δ(\'s3\', \'c\') = s3'

        expected_fsm = "\n".join([state, alphabet, initial_state, final_states, results])
        self.assertEqual(expected_fsm, str(fsm))

    def test_mod_4_calculator_valid_input(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)

        actual = fsm.mod_calculator("abcaa")
        self.assertEqual(3, actual)

        actual = fsm.mod_calculator("abcb")
        self.assertEqual(2, actual)

        actual = fsm.mod_calculator("abcba")
        self.assertEqual(3, actual)

    def test_mod_4_calculator_invalid_str_input(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        actual = fsm.mod_calculator("b1a")
        self.assertEqual(None, actual)

    def test_mod_4_calculator_invalid_final_state(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        actual = fsm.mod_calculator("abc")
        # Final state = s1 -> 1
        self.assertEqual(None, actual)

        actual = fsm.mod_calculator("abca")
        # Final state = s0 -> 0
        self.assertEqual(None, actual)

    def test_mod_4_calculator_invalid_input_type(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        actual = fsm.mod_calculator(11010)
        self.assertEqual(None, actual)

        actual = fsm.mod_calculator(True)
        self.assertEqual(None, actual)

    def test_mod_4_invalid_input_str_length(self):
        fsm = FiniteStateAutomata(states_4, alphabet_4, initial_state_4, final_states_4, transition_results_4)
        actual = fsm.mod_calculator("101010101010101010101010")
        self.assertEqual(None, actual)

    if __name__ == '__main__':
        unittest.main()
