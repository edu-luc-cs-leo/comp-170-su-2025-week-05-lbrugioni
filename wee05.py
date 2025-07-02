#Find the common character between two strings without including duplicates
#If there is no common characters, return None
def intersection(foo:str, bar:str) -> str | None:
    result=''
    seen_letters=''
    #Go through each letter in the first string  
    for letter in foo:
        if letter in bar and letter not in seen_letters:
            result+=letter
            seen_letters+=letter
    #if result is still empty return None 
    final_result=result if result !='' else None
    return final_result

#Find if string only contains letters uppercase or lowercase
def is_alphabetical(string:str) -> bool:
    #return true if string contains upper or lowercase letters 
    only_letters=True
    for character in string:
        ascii_value=ord(character)
        #checks if its not an uppercase or lowercase letter
        if not(65<=ascii_value<=90 or 97<=ascii_value<=122):
            only_letters=False
    return only_letters

#Create a palindrome which adds the reverse of the input string to itself 
def generate_palindrome(string:str) -> str | None:
    reversed_string=''
    #start at the last character of the string
    index=len(string)-1
    while index >=0:
        reversed_string+=string[index]
        index-=1
    #combines the orginal string with the reversed version of itself 
    palindrome=string+reversed_string
    #returns none if no input was given 
    final_result=palindrome if palindrome!=''else None
    return final_result

#Checks if the input is a palindrome
def is_palindrome(string:str) -> bool:
    cleaned=''
    for character in string:
        ascii_value=ord(character)
        if 65<=ascii_value<=90:
            cleaned+=chr(ascii_value +32)
        elif 97<=ascii_value<=122 or 48 <=ascii_value<=57:
            cleaned+=character
    left=0
    right=len(cleaned)-1
    result=True
    #compares characters from both ends until they meet in the middle 
    while left<right:
        if cleaned[left]!=cleaned[right]:
            result=False
        left+=1
        right-=1
    return result 

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
#
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
#
# Testing here is done a bit more formally than using simple print statements.
# This type of testing is called "Unit Testing" and can be extremely useful.
# Unit testing applies to small components of the software we write -- in this
# case the units tested are the individual methods we wrote.
#

import unittest

class TestStringMethods(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection("airplanes", "repairman"), "airpne")
        self.assertEqual(intersection("abc", "def"), "")
        self.assertEqual(intersection("hello", "hello"), "hello")
        self.assertEqual(intersection("aaaa", "aaa"), "a")
        self.assertEqual(intersection("", "abc"), None)
        self.assertEqual(intersection("abc", ""), None)
        self.assertEqual(intersection("", ""), None)
        self.assertEqual(intersection("abc", "cab"), "abc") # preserves order of `foo`
    def test_is_alphabetical(self):
        self.assertTrue(is_alphabetical("abcXYZ"))
        self.assertFalse(is_alphabetical("abc1"))
        self.assertFalse(is_alphabetical("hello!"))
        self.assertFalse(is_alphabetical(" "))
        self.assertFalse(is_alphabetical(""))
        self.assertFalse(is_alphabetical(None))
        self.assertTrue(is_alphabetical("ZzAaBb"))
    def test_letters_only(self):
        self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")
        self.assertEqual(letters_only("!@#$%^&*()"), "")
        self.assertEqual(letters_only(""), None)
        self.assertEqual(letters_only(None), None)
        self.assertEqual(letters_only("LettersONLY"), "LettersONLY")  
    def test_generate_palindrome(self):
        self.assertEqual(generate_palindrome("mice"), "miceecim")
        self.assertEqual(generate_palindrome("mad"), "madam")
        self.assertEqual(generate_palindrome("a"), "a")
        self.assertEqual(generate_palindrome(""), None)
        self.assertEqual(generate_palindrome(None), None)  
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Palindrome"))
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome(None))

# This allows the test to be run from the command line using `python -m unittest filename.py`
if __name__ == '__main__':
    unittest.main()