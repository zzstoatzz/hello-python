import ast
from pydantic import BaseModel
from typing import Optional, Callable, List

class Challenge(BaseModel):
    prompt: str
    expression: str
    expected_result: str
    pre_run: Optional[Callable] = None
    post_run: Optional[Callable] = None


def is_literal(node):
    """Check if the AST node is a literal (number, string, etc.)."""
    return isinstance(node, ast.Constant)

def is_simple_expression(user_input):
    """Check if the input is a simple expression, not a direct value."""
    try:
        parsed_input = ast.parse(user_input, mode='eval')
        return not is_literal(parsed_input.body)
    except SyntaxError:
        return False

def verify_expression(challenge_number: int, user_input: str, expected_result: str):
    try:
        if not is_simple_expression(user_input):
            return (
                f"Challenge {challenge_number}: Incorrect. "
                "Please provide a valid expression, not the direct answer."
            )

        user_result = eval(user_input)
        expected_evaluated = eval(expected_result)
        
        if user_result == expected_evaluated:
            return (f"Challenge {challenge_number}: Correct!")
        else:
            return (f"Challenge {challenge_number}: Incorrect. "
                    f"Your expression gave {user_result}, "
                    f"but expected {expected_evaluated}.")
    except (SyntaxError, TypeError, NameError) as e:
        match e:
            case SyntaxError():
                error_type = "Invalid syntax"
            case TypeError():
                error_type = "Type error"
            case NameError():
                error_type = "Name error"
        
        return (f"Challenge {challenge_number}: {error_type} in your expression - {e}")


def run_challenge(challenge_number: int, challenge: Challenge, max_retries: int = 3):
    retries = 0
    while retries < max_retries:
        user_input = input(challenge.prompt)
        result = verify_expression(
            challenge_number,
            user_input,
            challenge.expected_result
        )
        print(result + "\n")
        if "Correct!" in result:
            break
        retries += 1
        if retries < max_retries:
            print(f"Try again! Attempts remaining: {max_retries - retries}")
    if retries == max_retries:
        print(f"Challenge {challenge_number}: Let's move on for now, come back later!")

# Define the challenges
favorite_word = input("Enter your favorite word: ")
favorite_number = input("Enter your favorite number: ")
my_list = [favorite_word, favorite_number]

challenges: List[Challenge] = [
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

# Running the challenges
for i, challenge in enumerate(challenges, start=1):
    if challenge.pre_run:
        challenge.pre_run()

    run_challenge(i, challenge)

    if challenge.post_run:
        challenge.post_run()

print("Great job attempting the challenges! Remember, practice makes perfect.")
