"""
data/data_generators.py

This module provides utility functions for generating random data, specifically
for testing purposes within the Orange HRM application. The functions included
here can be used to create random names and employee IDs to facilitate the
population of test data.

Functions:
    - generate_random_name(): Generates a random first, middle, and last name.
    - generate_random_employee_id(): Generates a random 3-digit employee ID.
"""
import random
import string

def generate_random_name():
    """Generates random first, middle, and last names."""
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Fay", "Grace", "Hank"]
    middle_names = ["James", "Marie", "Lee", "Ray", "Louise", "Rose", "Jude", "Lynn"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]

    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    last_name = random.choice(last_names)

    return first_name, middle_name, last_name

def generate_random_employee_id():
    """Generate a random 3 digit employee ID."""
    return ''.join(random.choices(string.digits, k=3))  # 6-digit employee ID
