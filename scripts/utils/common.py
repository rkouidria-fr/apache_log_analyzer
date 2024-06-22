import json

def load_config(file_path: str):
    """
    Function that loads a JSON configuration file.

    Args:
        file_path (str): The path to the JSON configuration file.

    Returns:
        dict: The configuration dictionary.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def will_checker(user_answer: str) -> bool:
    """
    Function that returns true if the user respond by affirmative;

    Args:
        user_answer (str): The user input to check.

    Returns:
        bool: True if the user input is 'yes' or 'y', False otherwise.
    """
    return user_answer.lower() in ("yes", "y")