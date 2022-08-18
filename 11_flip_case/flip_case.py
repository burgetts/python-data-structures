def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_case = ''
    for char in phrase:
        if char == to_swap.upper():
            flipped_case += char.lower()
        elif char == to_swap.lower():
            flipped_case += char.upper()
        else:
            flipped_case += char
    return flipped_case