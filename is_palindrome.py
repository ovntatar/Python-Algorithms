def is_palindrome(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """

    # s[i] and s[j] are the next pair of characters to compare.
    i = 0
    j = len(s) - 1

    # The characters in s[:i] have been successfully compared to those in s[j:].
    while i < j and s[i] == s[j]:
	i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return j <= i

if __name__=="__main__":
	import doctest
        doctest.testmod()
        print is_palindrome('noon')
