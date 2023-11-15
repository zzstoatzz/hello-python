import ast
from pydantic import BaseModel
from typing import Optional, Callable

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

def setup_and_run_challenges(challenges: list[Challenge]):
    for i, challenge in enumerate(challenges, start=1):
        if challenge.pre_run:
            challenge.pre_run()

        run_challenge(i, challenge)

        if challenge.post_run:
            challenge.post_run()