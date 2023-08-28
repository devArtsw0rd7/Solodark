import random

def roll_d4(num_dice):
    return [random.randint(1, 4) for _ in range(num_dice)]

def roll_d6(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def roll_d8(num_dice):
    return [random.randint(1, 8) for _ in range(num_dice)]

def roll_d12(num_dice):
    return [random.randint(1, 12) for _ in range(num_dice)]

def roll_d20(num_dice):
    return [random.randint(1, 20) for _ in range(num_dice)]
