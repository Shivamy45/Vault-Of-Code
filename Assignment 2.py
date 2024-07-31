# 1. Write a program to count word frequencies in a given text.
def countWord(text, word):
    count = 0
    textList = text.split()
    for i in textList:
        if i == word:
            count += 1
    return count

text = "This is a word calculator. It calculates the frequency of a word in a given text."
word = "word"
print(countWord(text, word))


# 2. Palindrome Checker
# Write a program that check if a given word is palindrome
def checkPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(checkPalindrome("racecar"))
print(checkPalindrome("hello"))


# 3. List Manipulation
# Create a list of numbers, then write a program that prints the square of each number in the list.
def printSquare(numbers):
    for i in numbers:
        print(i**2, end=" ")
list = [1,2,3,4,5]
printSquare(list)