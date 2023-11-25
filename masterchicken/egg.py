def cook_egg(temp, time):
    """
    Cooks an egg based on the given temperature and time.

    Args:
        temp (float): The cooking temperature in degrees Celsius.
        time (int): The cooking time in minutes.

    Returns:
        str: A message indicating how the egg turned out.
    """
    if temp < 60:
        return "The egg is still raw."
    elif 60 <= temp < 70:
        if time < 3:
            return "The egg is still runny."
        elif 3 <= time < 5:
            return "The egg is cooked but still soft."
        else:
            return "The egg is overcooked and hard."
    elif 70 <= temp < 80:
        if time < 5:
            return "The egg is still runny."
        elif 5 <= time < 7:
            return "The egg is cooked but still soft."
        else:
            return "The egg is overcooked and hard."
    else:
        return "The egg is burnt."
