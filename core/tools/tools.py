def enumerate_languages_dict(languages):
    """
    Converts a comma-separated string of languages into an enumerated dictionary.

    Args:
        languages (str): A string containing languages separated by commas.

    Returns:
        dict_items: An iterable view of key-value pairs from the enumerated dictionary.
    """
    return dict(enumerate(languages.split(","))).items()

def format_languages_str(languages):
    """
    Formats an iterable of key-value pairs into a numbered list as a string.

    Args:
        languages (iterable): An iterable containing key-value pairs (e.g., from enumerate_languages_dict).

    Returns:
        str: A formatted string where each language is numbered in a new line.
    """
    return "\n".join(f"{key + 1}) {value}" for key, value in languages)
