def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    
    reverse_phrase = ''

    # Remove spaces
    phrase = phrase.replace(' ','')
    # Reverse word
    for i in range(1,len(phrase)+1):
        reverse_phrase += phrase[-i].lower()

    if reverse_phrase == phrase.lower():
        return True
    else: return False

    
    
