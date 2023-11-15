import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from utils import Challenge, setup_and_run_challenges

favorite_word = input("Enter your favorite word: ")
favorite_number = input("Enter your favorite number: ")
my_list = [favorite_word, favorite_number]

challenges = [
    Challenge(
        prompt=(
            f"Write an expression to reverse {favorite_word!r} "
            "(strings must be in quotes):"
        ),
        expression=f"'{favorite_word}'[::-1]",
        expected_result=f"'{favorite_word}'[::-1]"
    ),
    Challenge(
        prompt=f"Write an expression to multiply {favorite_number} by 7: ",
        expression=f"{favorite_number} * 7",
        expected_result=str(int(favorite_number) * 7)
    ),
    Challenge(
        prompt=(
            "Write an expression to create a new list by adding a new item"
            " to my_list, then return the length of the new list:"
        ),
        expression="len(my_list + ['new item'])",
        expected_result=str(len(my_list + ['new item'])),
        pre_run=lambda: print(f"Initial list: {my_list}")
    ),
    Challenge(
        prompt=(
            "Write a boolean expression to check if the length of"
            f" '{favorite_word}' equals {favorite_number}: "
        ),
        expression=f"len('{favorite_word}') == {favorite_number}",
        expected_result=str(len(favorite_word) == int(favorite_number))
    )
]

setup_and_run_challenges(challenges)