# encode = utf-8

def roll_dice(dice: str) -> tuple:
    """
    Simulate rolling dices
    :param dice: Dice expression, e.g., "2d6" means rolling 2 six-sided dice
    :return: A tuple containing total points and a list of individual dice results
    """
    import random
    # Parse dice expression
    try:
        num_dice, num_sides = map(int, dice.split('d'))
    except ValueError:
        raise ValueError("Invalid dice expression format, e.g., '2d6' means rolling 2 six-sided dice")

    # Simulate rolling the dice and store individual results
    dice_results = [random.randint(1, num_sides) for _ in range(num_dice)]

    # Calculate total as the sum of all dice results
    total = sum(dice_results)

    return total, dice_results
