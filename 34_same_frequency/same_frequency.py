def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    def frequency(num):
        num = str(num)
        freq = {}
        for item in num:
            freq[item] = num.count(item)
        return freq
    
    if frequency(num1) == frequency(num2):
        return True
    else: return False
