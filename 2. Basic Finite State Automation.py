initial_state = 'q0'
final_state = 'q2'
Transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
input_string = input("Enter the String = ")
current_state = initial_state
for char in input_string:
    current_state = Transitions[current_state].get(char, initial_state)
result = "accepted" if current_state == final_state else "not accepted"
print(f"'{input_string}' is {result}.")
