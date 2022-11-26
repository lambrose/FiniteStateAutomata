def convert_list_to_str(list_value: list) -> str:
    # Concatenate all elements of a list to a single string that is separated by a comma
    return ", ".join(list_value)


def format_transaction_str(dictionary: dict) -> str:
    # Return a concatenated string that is separated by a semicolon
    return "; ".join(f"δ{key} = {value}" for key, value in dictionary.items())
