###############################################
# Python Basics: Understanding Data Types

## Throughout this file I'll use this f-string trick to print out
## the expression and the result of the expression at the same time.

## you basically just put an = after the expression and it will print
## the expression and the result of the expression

### for example:
# if i had a simple expression like 1 == 1 (which says 1 is equal to 1)
# then i could say: print(f"{1 == 1=}") and it would print: 1 == 1 = True

# Introduction to Strings
favorite_word = input("Enter a favorite word: ")

while len(favorite_word) < 3:
    favorite_word = input("Enter a favorite word (at least 3 characters): ")

print(f"{favorite_word=}")
print(f"Your word is a string: {isinstance(favorite_word, str)=}")
input("\nStrings come with a lot of built-in methods. Press enter to see an example.")
print(f"Uppercase: {favorite_word.upper()=}")
print(f"Titlized: {favorite_word.title()=}")
input("\nYou can slice strings with [start:stop:step]. Press enter to see an example.")
print(f"First letter: {favorite_word[0]=}")
print(f"Last letter: {favorite_word[-1]=}")
print(f"First 3 letters: {favorite_word[:3]=}")
print(f"Last 3 letters: {favorite_word[-3:]=}")
print(f"Reversed: {favorite_word[::-1]=}")
print(f"Length: {len(favorite_word)=}")
print(f"Adding two words: {(favorite_word + favorite_word)=}")


# Introduction to Numbers
while True:
    favorite_number = input("\nEnter your favorite number: ")
    
    if favorite_number.isnumeric():
        favorite_number = int(favorite_number)
        break
    else:
        print("That's not a number! Try again.")

print(f"{favorite_number=}")
input("\nNumbers in Python can be manipulated in many ways. Press enter to see")
print(f"Multiplied by 3: {favorite_number * 3=}")
print(f"Divided by 2: {favorite_number / 2=}")
print(f"Raised to the power of 2: {favorite_number ** 2=}")
input("\nPython can also handle division details. Press enter to see.")
print(f"Floor division by 2: {favorite_number // 2=}")
print(f"Remainder when divided by 2: {favorite_number % 2=}")

# Introduction to Lists
print("\nLists: A collection of items.")
my_list = [favorite_word, favorite_number]
print(f"Initial list: {[favorite_word, favorite_number]=}")
input("\nLists can be modified and accessed in various ways. Press enter to continue.")
new_item = input("Add a new item to your list: ")
my_list.append(new_item)
print(f"Updated list (my_list.append(new_item)): {my_list=}")
print(f"Second item in the list: {my_list[1]=}")
input("\nLists can also be sliced like strings. Press enter to see.")
print(f"First two items: {my_list[:2]=}")
my_list.reverse() # This method reverses the list in place
print(f"List in reverse (after my_list.reverse()): {my_list=}")
print(f"Adding two lists: {my_list + my_list=}")

# Introduction to Booleans
input("\nBooleans: A data type that is either True or False. Press enter to continue.")
print(f"Is your word longer than 5 characters? {len(favorite_word) > 5=}")
input("\nBooleans are often used in comparisons. Press enter to see examples.")
print(f"Is your number even? {favorite_number % 2 == 0=}")
print(f"Does your list have more than 3 items? {len(my_list) > 3=}")
print(
    "\nYou can also do logic with booleans.\n\n"
    "e.g. Is your word longer than 5 characters and your number even?"
    f"{len(favorite_word) > 5 and favorite_number % 2 == 0=}"
)