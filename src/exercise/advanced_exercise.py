from src.utils.string_formatter import convert_list_to_str, format_transaction_str


class FiniteStateAutomata:
    # Arbitrary value - for scenario purposes
    max_string_length = 10

    def __init__(self, states: list, alphabet: list, initial_state: str, final_states: list, results: dict):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_results = results

    @property
    def states(self) -> list:
        return self.__states

    @states.setter
    def states(self, value: list) -> None:
        self.__states = value

    @property
    def alphabet(self) -> list:
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, value: list) -> None:
        self.__alphabet = value

    @property
    def initial_state(self) -> str:
        return self.__initial_state

    @initial_state.setter
    def initial_state(self, value: str) -> None:
        self.__initial_state = value

    @property
    def final_states(self) -> list:
        return self.__final_states

    @final_states.setter
    def final_states(self, value: list) -> None:
        self.__final_states = value

    @property
    def transition_results(self) -> dict:
        return self.__transition_results

    @transition_results.setter
    def transition_results(self, value: dict) -> None:
        self.__transition_results = value

    # Construct a dictionary {key = (state, alphabet option), value = result state}
    def get_transition(self) -> dict:
        transition = {}
        # Add the transition to the dictionary if a valid alphabet option is used
        for alphabet in self.alphabet:
            for index, result in enumerate(self.transition_results.get(alphabet)):
                transition[(self.states[index], alphabet)] = result
        return transition

    def get_transition_map(self) -> dict:
        # Return a dictionary of the state and corresponding index
        return {state: index for index, state in enumerate(self.states)}

    def mod_calculator(self, input_val: str) -> int:
        try:
            # Raise an error if the input is not a string
            if type(input_val) is not str:
                raise TypeError("Invalid string input type error!")
            elif len(input_val) > self.max_string_length:
                raise ValueError("Invalid input string. Length too long!")
            else:
                def mod_recursion(position: str, val: str) -> int:
                    if len(val) == 0:
                        # Raise an error if the last state position is not an acceptable final state
                        if position not in self.final_states:
                            raise ValueError("String character is not present in the final state options!")
                        return self.get_transition_map().get(position)

                    # Raise an error if the character is not a valid alphabet character.
                    if val[0] not in self.alphabet:
                        raise ValueError("String character is not present in the alphabet options!")

                    # After every recursive call get the new state position after a transition
                    position = self.get_transition().get((position, val[0]))

                    # On every call the string input it being shortened by one
                    return mod_recursion(position, val[1:])

                return mod_recursion(self.initial_state, input_val)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)

    # Return a string representation of the finite automaton class.
    def __str__(self):
        states = f"Q = ({convert_list_to_str(self.states)})"
        alphabet = f"Σ = ({convert_list_to_str(self.alphabet)})"
        initial_state = f"q0 = {self.initial_state}"
        final_states = f"F = ({convert_list_to_str(self.final_states)})"
        transition = format_transaction_str(self.get_transition())
        # Concatenate all elements of a list to a single string that is separated by a new line character
        return "\n".join([states, alphabet, initial_state, final_states, transition])
