def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    If numbers is empty, return False
    If the number of even numbers is odd, return False
    If the number of even numbers is O, return False
    If the number of even numbers is even, return True
    """
    #  The isinstance() function in Python is used to determine whether an objec
    #  is an instance of a particular class. It allows you to check if an object
    #  belongs to a specific class or any of its derived classes.

    if isinstance(numbers, list):

        evens = len([n for n in numbers if n % 2 == 0])
      #   evens = 0
      #   for number in numbers:
      #       if number % 2 == 0:
      #           evens += 1
        # ====================================
        return True if evens and evens % 2 == 0 else False
      #   if evens:
      #       return evens % 2 == 0
      #   else:
      #       return False
    else:
        raise TypeError(
            f"A list was not passed into the function: {numbers}")


# when Python runs a file directly, it names it __main__ and any code
# beneath the if statement will only be run if the name of the file is __main__.
if __name__ == "__main__":
    print(even_number_of_evens([2, 4]))
