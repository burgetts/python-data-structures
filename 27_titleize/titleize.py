def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = ''
    phrase = list(phrase.split(' '))
    # Capitalize first of each phrase, lowercase the rest
    for word in phrase:
        for i in range(len(word)):
            if i ==0:
                new_phrase += word[i].upper()
            else:
                new_phrase += word[i].lower()
        new_phrase += ' '
    return new_phrase.rstrip(' ')
   
                

    