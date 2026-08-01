"""
PDP Practice Problem Bank — Problems 1-38
===========================================================================
Programming & Design Principles (5N2927) — general Python practice.

Provenance: combined and renumbered from 8 separate files found in an
uploaded `python.zip` (2026-08-01): practice-problems-1-2.py, -2.py, -3.py,
-4.py, -5.py, -6.py, -7.py, -other.py. Problems 23-38 already carried
"Problem N" numbering in their source docstrings; problems 1-22 didn't, and
are numbered here to make the whole bank one continuous sequence. A near-
duplicate draft of problems 1-7 (practice-problems-1_3.py, containing messy
in-progress student annotations rather than a distinct problem set) was
found and intentionally excluded — see the upload manifest in
`planning/2026-08-01-upload-manifest.md` for details.

All problems are blank TODO stubs (student-facing), not solutions.
===========================================================================

Section A: Arithmetic Basics (Problems 1-7)
Section B: Patterns, Conversions and Strings (Problems 8-22)
Section C: String & Number Utilities (Problems 23-38, class-based)
"""

from typing import List


# ===========================================================================
# Section A: Arithmetic Basics (Problems 1-7)
# ===========================================================================

def print_hello_name(name: str) -> None:
    """
    Problem 1: Print 'Hello' and your name in separate lines.

    Args:
        name (str): Your name

    Expected Output:
        Hello
        <your name>
    """
    # TODO: Print "Hello" and the name on separate lines
    pass


def sum_two_numbers(num1: float, num2: float) -> float:
    """
    Problem 2: Calculate and return the sum of two numbers.

    Args:
        num1 (float): First number
        num2 (float): Second number

    Returns:
        float: Sum of the two numbers
    """
    # Your code here
    pass


def divide_numbers(num1: float, num2: float) -> float:
    """
    Problem 3: Calculate and return the result of dividing first number by second number.

    Args:
        num1 (float): Dividend (number to be divided)
        num2 (float): Divisor (number to divide by)

    Returns:
        float: Result of division
    """
    # TODO: Implement division (remember to handle division by zero!)
    pass


def calculate_operations() -> list[float]:
    """
    Problem 4: Calculate the results of the following operations:
    1. -1 + 4 * 6
    2. (35 + 5) % 7
    3. 14 + -4 * 6 / 11
    4. 2 + 15 / 6 * 1 - 7 % 2

    Returns:
        list[float]: List containing the results of all operations
    """
    # TODO: Calculate each operation and return results in a list
    pass


def swap_numbers(a: float, b: float) -> tuple[float, float]:
    """
    Problem 5: Swap two numbers and return them.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        tuple[float, float]: Tuple containing the swapped numbers (b, a)

    Example:
        Input: a=5, b=6
        Output: (6, 5)
    """
    # Your code here: Swap the numbers
    pass


def multiply_three_numbers(num1: float, num2: float, num3: float) -> float:
    """
    Problem 6: Multiply three numbers input by the user.

    Args:
        num1 (float): First number
        num2 (float): Second number
        num3 (float): Third number

    Returns:
        float: Product of the three numbers

    Example:
        Input: 2, 3, 6
        Output: 36
    """
    # TODO: Calculate and return the product
    pass


def perform_arithmetic_operations(num1: float, num2: float) -> dict[str, float]:
    """
    Problem 7: Perform basic arithmetic operations on two numbers.

    Args:
        num1 (float): First number
        num2 (float): Second number

    Returns:
        dict[str, float]: Dictionary containing results of:
            - addition
            - subtraction
            - multiplication
            - division
            - modulus

    Example:
        Input: 25, 4
        Output: {
            'addition': 29,
            'subtraction': 21,
            'multiplication': 100,
            'division': 6.25,
            'modulus': 1
        }
    """
    # TODO: Implement all arithmetic operations and return in dictionary
    pass


# ===========================================================================
# Section B: Patterns, Conversions and Strings (Problems 8-22)
# ===========================================================================

def print_multiplication_table(number: int) -> None:
    """
    Problem 8: Print the multiplication table for a given number from 0 to 10.

    Args:
        number (int): The number to create multiplication table for

    Expected Output:
        5 * 0 = 0
        5 * 1 = 5
        5 * 2 = 10
        ...
        5 * 10 = 50
    """
    # TODO: Print multiplication table from 0 to 10
    pass


def calculate_average(num1: float, num2: float, num3: float, num4: float) -> float:
    """
    Problem 9: Calculate the average of four numbers.

    Args:
        num1 (float): First number
        num2 (float): Second number
        num3 (float): Third number
        num4 (float): Fourth number

    Returns:
        float: Average of the four numbers

    Example:
        Input: 10, 15, 20, 30
        Output: 18.75
    """
    # TODO: Calculate and return the average of the four numbers
    pass


def calculate_special_operations(x: float, y: float, z: float) -> tuple[float, float]:
    """
    Problem 10: Calculate (x+y)*z and x*y + y*z for three numbers.

    Args:
        x (float): First number
        y (float): Second number
        z (float): Third number

    Returns:
        tuple[float, float]: ((x+y)*z, x*y + y*z)

    Example:
        Input: x=5, y=6, z=7
        Output: (77, 72)  # First number is (5+6)*7, second is 5*6 + 6*7
    """
    # TODO: Calculate both expressions and return them in a tuple
    pass


def create_age_message(age: int) -> str:
    """
    Problem 11: Create a message saying "You look older than X" where X is the input age.

    Args:
        age (int): The person's age

    Returns:
        str: Message about looking older than the given age

    Example:
        Input: 25
        Output: "You look older than 25"
    """
    # TODO: Return the appropriate message
    pass


def display_number_pattern(number: int) -> tuple[str, str, str, str]:
    """
    Problem 12: Create four strings that display a number in different patterns.
    The number should appear:
    - Four times with spaces between each
    - Four times with no spaces between
    - Repeated twice (with and without spaces)

    Args:
        number (int): The number to display

    Returns:
        tuple[str, str, str, str]: Four strings containing the number patterns

    Example:
        Input: 25
        Output: ("25 25 25 25", "25252525", "25 25 25 25", "25252525")
    """
    # TODO: Create and return the four pattern strings
    pass


def print_number_rectangle(number: int) -> None:
    """
    Problem 13: Print a rectangle pattern using a number (3 columns wide and 5 rows tall).

    Args:
        number (int): The number to use in the pattern

    Expected Output (for input 5):
        555
        5 5
        5 5
        5 5
        555
    """
    # TODO: Print the rectangle pattern
    pass


def convert_temperature(celsius: float) -> tuple[float, float]:
    """
    Problem 14: Convert Celsius temperature to Kelvin and Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        tuple[float, float]: (kelvin, fahrenheit)

    Example:
        Input: 30
        Output: (303.15, 86.0)
    """
    # TODO: Convert celsius to kelvin and fahrenheit
    # Hint: Kelvin = Celsius + 273.15
    #       Fahrenheit = (Celsius * 9/5) + 32
    pass


def remove_character(text: str, position: int) -> str:
    """
    Problem 15: Remove a character at the specified position from a string.

    Args:
        text (str): Input string
        position (int): Position of character to remove (0-based index)

    Returns:
        str: String with character removed

    Example:
        Input: text="w3resource", position=2
        Output: "w3esource"
    """
    # TODO: Remove character at given position and return modified string
    pass


def swap_first_last_chars(text: str) -> str:
    """
    Problem 16: Create a new string with the first and last characters swapped.

    Args:
        text (str): Input string

    Returns:
        str: String with first and last characters swapped

    Examples:
        Input: "Python"
        Output: "nythoP"

        Input: "w3resource"
        Output: "e3resourcw"
    """
    # TODO: Swap first and last characters and return modified string
    pass


def wrap_first_char(text: str) -> str:
    """
    Problem 17: Create a new string with the first character added at front and back.
    String must be length 1 or more.

    Args:
        text (str): Input string (length >= 1)

    Returns:
        str: Modified string with first character added at both ends

    Example:
        Input: "Python"
        Output: "PythonP"

        Input: "The quick brown fox"
        Output: "TThe quick brown foxT"
    """
    # TODO: Add first character to beginning and end of string
    pass


def check_negative_positive(num1: int, num2: int) -> bool:
    """
    Problem 18: Check if one number is negative and one is positive.

    Args:
        num1 (int): First integer
        num2 (int): Second integer

    Returns:
        bool: True if one is negative and one is positive, False otherwise

    Examples:
        Input: -5, 25
        Output: True

        Input: 5, 25
        Output: False

        Input: -5, -25
        Output: False
    """
    # TODO: Check if one number is negative and one is positive
    pass


def compute_triple_sum(num1: int, num2: int) -> int:
    """
    Problem 19: Compute the sum of two integers. If the values are the same,
    return triple their sum.

    Args:
        num1 (int): First integer
        num2 (int): Second integer

    Returns:
        int: Sum of numbers, or triple the sum if numbers are equal

    Examples:
        Input: 5, 5
        Output: 30  # (5 + 5) * 3

        Input: 5, 6
        Output: 11  # 5 + 6
    """
    # TODO: Return triple sum if numbers are equal, regular sum otherwise
    pass


def get_absolute_difference(num1: int, num2: int) -> int:
    """
    Problem 20: Get absolute difference between two numbers. Return double the absolute
    difference if first number is greater than second number.

    Args:
        num1 (int): First integer
        num2 (int): Second integer

    Returns:
        int: Absolute difference or double the absolute difference

    Examples:
        Input: 25, 15
        Output: 20  # (25 - 15) * 2

        Input: 15, 25
        Output: 10  # |15 - 25|
    """
    # TODO: Calculate absolute difference and double it if num1 > num2
    pass


def check_sum_twenty(num1: int, num2: int) -> bool:
    """
    Problem 21: Check if one of the numbers is 20 or if their sum is 20.

    Args:
        num1 (int): First integer
        num2 (int): Second integer

    Returns:
        bool: True if one number is 20 or sum is 20, False otherwise

    Examples:
        Input: 20, 5
        Output: True  # One number is 20

        Input: 15, 5
        Output: True  # Sum is 20

        Input: 15, 6
        Output: False # Neither number is 20 and sum isn't 20
    """
    # TODO: Check if either number is 20 or if their sum is 20
    pass


def is_within_twenty(number: int) -> bool:
    """
    Problem 22: Check if the given integer is within 20 of 100 or 200.

    Args:
        number (int): Integer to check

    Returns:
        bool: True if number is within 20 of 100 or 200, False otherwise

    Examples:
        Input: 115
        Output: True  # Within 20 of 100

        Input: 190
        Output: True  # Within 20 of 200

        Input: 25
        Output: False # Not within 20 of either 100 or 200
    """
    # TODO: Check if number is within 20 of either 100 or 200
    pass


# ===========================================================================
# Section C: String & Number Utilities (Problems 23-38)
# ===========================================================================

class StringAndNumberExercises:
    @staticmethod
    def convert_to_lowercase(input_str: str) -> str:
        """
        Problem 23: Write a program to convert a given string into lowercase.

        Example:
            Input: "Write A Python PROGRAM"
            Output: "write a python program"

        Args:
            input_str: String to convert to lowercase

        Returns:
            Lowercase version of the input string
        """
        # TODO: Write your code here to convert the string to lowercase
        pass

    @staticmethod
    def find_longest_word(sentence: str) -> str:
        """
        Problem 24: Find the longest word in a string.

        Example:
            Input: "Write a Python Program to display the following pattern"
            Output: "following"

        Note: If there are multiple words with the same length, return the first one.

        Args:
            sentence: Input string to analyze

        Returns:
            The longest word in the string
        """
        # TODO: Write your code here to find the longest word
        pass

    @staticmethod
    def get_odd_numbers() -> List[int]:
        """
        Problem 25: Generate all odd numbers from 1 to 99.
        The function should return a list of odd numbers that can be printed one per line.

        Example Output: [1, 3, 5, ..., 97, 99]

        Returns:
            List of all odd numbers from 1 to 99
        """
        # TODO: Write your code here to generate odd numbers
        pass

    @staticmethod
    def compute_prime_sum() -> int:
        """
        Problem 26: Compute the sum of the first 500 prime numbers.

        Expected Output: 824693

        Returns:
            Sum of first 500 prime numbers
        """
        # TODO: Write your code here to compute the sum of first 500 primes
        # Hint: First create a method to check if a number is prime
        # Then find the first 500 primes and sum them
        pass

    @staticmethod
    def sum_of_digits(number: int) -> int:
        """
        Problem 27: Compute the sum of an integer's digits.

        Example:
            Input: 12
            Output: 3 (because 1 + 2 = 3)

        Args:
            number: Integer whose digits should be summed

        Returns:
            Sum of the digits
        """
        # TODO: Write your code here to sum the digits
        pass

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Helper method: Check if a number is prime.

        Args:
            number: Number to check for primality

        Returns:
            True if the number is prime, False otherwise
        """
        # TODO: Implement prime number check if needed for compute_prime_sum
        pass


class StringAndArrayExercises:
    @staticmethod
    def reverse_words(sentence: str) -> str:
        """
        Problem 28: Reverse the words of a sentence.

        Example:
            Input: "Display the pattern like pyramid using the alphabet."
            Output: "alphabet. the using pyramid like pattern the Display"

        Note: Preserve the original punctuation and spacing between words.

        Args:
            sentence: The input sentence to reverse

        Returns:
            String with words in reverse order
        """
        # TODO: Write your code here to reverse the words
        pass

    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        Problem 29: Find the size of a specified file in bytes.

        Example:
            Input: "example.txt"
            Output: 31 (bytes)

        Note: Make sure to handle cases where the file doesn't exist

        Args:
            file_path: Path to the file to check

        Returns:
            Size of the file in bytes, or -1 if file doesn't exist
        """
        # TODO: Write your code here to get file size
        # Remember to use try-except for file operations
        pass

    @staticmethod
    def hex_to_decimal(hex_number: str) -> int:
        """
        Problem 30: Convert a hexadecimal number to decimal.

        Example:
            Input: "4B0"
            Output: 1200

        Note: Handle both uppercase and lowercase hex digits

        Args:
            hex_number: String representation of hexadecimal number

        Returns:
            Decimal (base-10) value of the number
        """
        # TODO: Write your code here to convert hex to decimal
        pass

    @staticmethod
    def multiply_arrays(array1: List[int], array2: List[int]) -> List[int]:
        """
        Problem 31: Multiply corresponding elements of two integer arrays.

        Example:
            Input arrays: [1, 3, -5, 4] and [1, 4, -5, -2]
            Output: [1, 12, 25, -8]

        Note: Assume both arrays have the same length

        Args:
            array1: First array of integers
            array2: Second array of integers

        Returns:
            List containing products of corresponding elements
        """
        # TODO: Write your code here to multiply corresponding elements
        pass

    @staticmethod
    def repeat_last_four(text: str) -> str:
        """
        Problem 32: Create a string of four copies of the last four characters.
        If the string is less than 4 characters, return the original string.

        Example:
            Input: "The quick brown fox jumps over the lazy dog."
            Output: "dog.dog.dog.dog."

        Args:
            text: Input string

        Returns:
            Four copies of last four chars or original string if length < 4
        """
        # TODO: Write your code here to repeat the last four characters
        pass


class NumberAndStringChecks:
    @staticmethod
    def is_multiple_of_3_or_7(number: int) -> bool:
        """
        Problem 33: Check if a given positive number is a multiple of 3 or 7.

        Examples:
            >>> is_multiple_of_3_or_7(15)
            True  # because 15 is a multiple of 3
            >>> is_multiple_of_3_or_7(14)
            True  # because 14 is a multiple of 7
            >>> is_multiple_of_3_or_7(8)
            False

        Args:
            number: Positive integer to check

        Returns:
            True if the number is a multiple of 3 or 7, false otherwise
        """
        # TODO: Write your code here to check if number is multiple of 3 or 7
        pass

    @staticmethod
    def starts_with_word(text: str, word: str) -> bool:
        """
        Problem 34: Check if a string starts with a specified word.

        Examples:
            >>> starts_with_word("Hello how are you?", "Hello")
            True
            >>> starts_with_word("Good morning!", "Hello")
            False

        Note: The check should be case-sensitive

        Args:
            text: String to check
            word: Word to look for at the start

        Returns:
            True if the string starts with the specified word, false otherwise
        """
        # TODO: Write your code here to check if text starts with word
        pass

    @staticmethod
    def check_number_range(num1: int, num2: int) -> bool:
        """
        Problem 35: Check if one number is less than 100 and another is greater than 200.

        Examples:
            >>> check_number_range(75, 250)
            True
            >>> check_number_range(150, 250)
            False

        Note: Either number can be the one less than 100 while the other is greater than 200

        Args:
            num1: First number to check
            num2: Second number to check

        Returns:
            True if one number is < 100 and the other is > 200, false otherwise
        """
        # TODO: Write your code here to check the number ranges
        pass

    @staticmethod
    def is_in_range(num1: int, num2: int) -> bool:
        """
        Problem 36: Check if either of two integers is in the range -10 to 10 (inclusive).

        Examples:
            >>> is_in_range(-5, 8)
            True  # both numbers are in range
            >>> is_in_range(-15, 15)
            False  # neither number is in range

        Note: The range includes both -10 and 10

        Args:
            num1: First number to check
            num2: Second number to check

        Returns:
            True if either number is in the range -10 to 10, false otherwise
        """
        # TODO: Write your code here to check if either number is in range -10 to 10
        pass


def find_most_frequent_number(numbers: list[int]) -> int:
    """
    Problem 37: Given a list of integers, find the number that appears most frequently.
    If there are multiple numbers that appear the same number of times, return the smallest one.

    Example:
        Input: [1, 2, 3, 2, 4, 2, 1]
        Output: 2 (appears 3 times)

    Parameters:
        numbers (list[int]): List of integers
    Returns:
        int: The most frequent number in the list
    """
    # TODO: Write your solution here
    pass


def is_valid_palindrome(s: str) -> bool:
    """
    Problem 38: Check if a string is a valid palindrome after converting all characters
    to lowercase and removing all non-alphanumeric characters.

    Example:
        Input: "A man, a plan, a canal: Panama"
        Output: True

    Parameters:
        s (str): Input string to check
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Your code here
    pass


if __name__ == "__main__":
    # Uncomment individual calls as you implement each problem.
    pass
