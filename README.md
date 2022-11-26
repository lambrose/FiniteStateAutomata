# FiniteStateAutomata

Generate a finite state automata.

## Standard Exercise
    - Loop method: This was my inital solution.
        -  Simpler code
    - Recursion method: This is my final solution.
        - Average faster runtime
    
## Advanced Exercise
    - A software module for generating an FSM.
    - The module is called FiniteStateAutomata.

## Python
Version:  Python 3.8.9

## Create a 'venv'
1. Unix/MacOS: python3 -m venv env
2. Windows: py -m venv env

## Usage

```python
import FiniteStateAutomata

# Create an instance
fsm = FiniteStateAutomata(states, alphabet, initial_state, final_states, transition_results)

e.g. input:
    states = ["s0", "s1", "s2"]
    alphabet = ["0", "1"]
    initial_state = "s0"
    final_states = ["s0", "s1", "s2"]
    transition_results = {"0": ["s0", "s2", "s1"], "1": ["s1", "s0", "s2"]}


# return a string representation of the 5 tuple fsm
fsm or str(fsm)

# return fsm transitions
fsm.get_transition()

# return fsm transitions map
fsm.get_transition_map()

# returns the calculated output, i.e. an integer or None type
fsm.mod_calculator(input_string)
```