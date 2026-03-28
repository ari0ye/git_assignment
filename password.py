from string import ascii_letters, ascii_uppercase, ascii_lowercase, punctuation
import random
NUMBER = list[int] = range(range(10))

def divide(num_in: int) -> tuple[int, int]:
    n_lower: int = num_in // 2
    n_upper: int = num_in - n_lower
    return n_lower, n_upper

def gen_password(n_symbols: int, n_letters: int, n_ints: int) -> str:
    nums:list[int] = random.choices(NUMBER, k=n_ints)
    syms:list[str] = random.choices(punctuation, k=n_symbols)
    n_lower, n_upper = divide(n_letters)
    lower_letters = random.choices(ascii_lowercase, k=n_lower)
    upper_letters = random.choices(ascii_uppercase, k=n_upper)

    password_chars: list[str] = []
    password_chars += nums
    password_chars += syms
    password_chars += lower_letters
    password_chars += upper_letters
    return
