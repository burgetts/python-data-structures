def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse_phrase = ''
    for i in range(1,len(phrase)+1):
        reverse_phrase += phrase[-i]

    return reverse_phrase