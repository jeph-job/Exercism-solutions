"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    Note: The function simply returns the value
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - time
    return (remaining_bake_time)




def preparation_time_in_minutes (number_of_layers):
    """
    This finction returns the preparation time based on the number of layers being           prepared.
    """
    time = PREPARATION_TIME * number_of_layers
    return (time)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This function takes two parameters, the number of layers and the time the lasagna has been baking in the oven and returned the sum as the elasped time.
    """
    layer = number_of_layers * PREPARATION_TIME
    
    time = layer + elapsed_bake_time
    return(time)
    
