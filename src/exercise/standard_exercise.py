class ModThree:
    initial_state = "s0"
    alphabet = ["0", "1"]
    final_state = ["s0", "s1", "s2"]
    transition = {
        ("s0", "0"): "s0", ("s0", "1"): "s1",
        ("s1", "0"): "s2", ("s1", "1"): "s0",
        ("s2", "0"): "s1", ("s2", "1"): "s2"
    }
    transition_map = {
        "s0": 0,
        "s1": 1,
        "s2": 2
    }

    # Arbitrary value - for scenario purposes
    max_string_length = 10

    def __init__(self):
        pass

    # Loop method -> Ran 10 tests in 0.011s
    def mod_three_loop(self, input_val: str) -> int:
        try:
            # Raise an error if the input is not a string
            if type(input_val) is not str:
                raise TypeError("Invalid string input type error!")
            elif len(input_val) > self.max_string_length:
                raise ValueError("Invalid input string. Length too long!")
            else:
                position = self.initial_state

                for val in input_val:
                    # Raise an error if the character is not a valid alphabet character.
                    if val not in self.alphabet:
                        raise ValueError("Character is not present in the alphabet options!")
                    # After every iteration get the new state position after a transition
                    position = self.transition.get((position, val))
                # Raise an error if the last state position is not an acceptable final state
                if position not in self.final_state:
                    raise ValueError("Character is not present in the final state options!")
                return self.transition_map.get(position)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)

    # Recursion method -> Ran 10 tests in 0.008s
    def mod_three(self, input_val: str) -> int:
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
                        if position not in self.final_state:
                            raise ValueError("String character is not present in the final state options!")
                        return self.transition_map.get(position)

                    # Raise an error if the character is not a valid alphabet character.
                    if val[0] not in self.alphabet:
                        raise ValueError("String character is not present in the alphabet options!")

                    # After every recursive call get the new state position after a transition
                    position = self.transition.get((position, val[0]))

                    # On every call the string input it being shortened by one
                    return mod_recursion(position, val[1:])

                return mod_recursion(self.initial_state, input_val)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)
