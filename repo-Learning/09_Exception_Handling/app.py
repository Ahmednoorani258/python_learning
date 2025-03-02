# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except:
#     print("An error occurred!")
    
    
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
    
    
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"Division successful. Result: {result}")

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("This will always execute.")
    
    

# def divide_numbers(a, b):
#     try:
#         result = a / b  # Test this block for errors
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     except TypeError:
#         print("Error: Invalid input type. Numbers required.")
#     else:
#         print(f"Division successful. Result: {result}")
#     finally:
#         print("Operation complete.")


# # Test cases
# divide_numbers(10, 2)  # Successful division
# divide_numbers(10, 0)  # ZeroDivisionError
# divide_numbers(10, "2")  # TypeError








# import random
# from typing import Tuple, Dict, List

# def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
#     """Generates a list of random number pairs."""
#     try:
#         if not isinstance(num_samples, int) or num_samples <= 0:
#             raise ValueError("Number of samples must be a positive integer.")
#         data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
#         return data
#     except ValueError as ve:
#         print(f"Error: {ve}")
#         return []  # Return empty list on error
#     except Exception as e: # Catch any other unexpected errors
#         print(f"An unexpected error occurred: {e}")
#         return []


# def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
#     """Calculates the ratio of the first number to the second in each pair."""
#     ratios = []
#     try:
#         for pair in data:
#             num1, num2 = pair
#             if num2 == 0:
#                 raise ZeroDivisionError("Cannot divide by zero.")
#             if not isinstance(num1,int) or not isinstance(num2,int):
#                 raise TypeError("Input data must be integers.")
#             ratio = num1 / num2
#             ratios.append(ratio)
#         return ratios
#     except ZeroDivisionError as zde:
#         print(f"Error: {zde}")
#         return []  # Return empty list on error.
#     except TypeError as te:
#         print(f"Error: {te}")
#         return []
#     except Exception as e:
#         print(f"An unexpected error occurred during ratio calculation: {e}")
#         return []


# def process_data(num_samples: int) -> List[float]:
#     """Combines data generation and ratio calculation with comprehensive error handling."""

#     data = generate_random_data(num_samples)
#     if not data: # check if generate_random_data returns an empty list which means it had an error
#         return []

#     ratios = calculate_ratios(data)

#     return ratios

# # Example usage with error handling
# try:
#   num_samples = 55555555
#   results = process_data(num_samples)

#   if results:
#     print("Calculated ratios:", results)
#   else: # if process_data returned an empty list it means there was some error
#       print("Data processing failed due to an error.")

# except Exception as e: # catching unexpected errors
#     print(f"An unexpected error occurred: {e}")

# # example of invalid input
# results = process_data(-5)
# if not results:
#   print("Negative number of samples, data processing failed.")

# results = process_data("abc")
# if not results:
#     print("Invalid input type, data processing failed.")

# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     result = num1 / num2
# except ValueError:
#     print("Error: Invalid input. Please enter numbers.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# else:
#     print(f"The result is: {result}")
# finally:
#     print("Thank you for using the program!")

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed!")  # Raising an exception
#     return a / b

# print(divide(10, 2))  # Output: 5.0
# print(divide(5, 0))   # Raises: ValueError: Division by zero is not allowed!


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed!")
#     return a / b

# try:
#     result = divide(5, 0)  # This will raise an exception
#     print(result)  # This line won't run if exception occurs
# except ValueError as e:
#     print(f"Error: {e}")  # Output: Error: Division by zero is not allowed!

# print("Program continues...")  # This line will always execute





# class NegativeNumberError(Exception):
#     """Custom exception for negative numbers"""
#     pass

# def check_positive(n):
#     if n < 0:
#         raise NegativeNumberError("Negative numbers are not allowed!")
#     return f"{n} is positive"

# try:
#     print(check_positive(-5))  # Raises NegativeNumberError
# except NegativeNumberError as e:
#     print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!


