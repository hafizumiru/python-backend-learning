def add(*number):
    total = number[0]   
    for num in number[1:]:
        total += num
    return total

def subtract(*number):
    total = number[0]   
    for num in number[1:]:
        total -= num
    return total

def multiply(*number):
    total = number[0]
    for num in number[1:]:
        total *= num
    return total

def divide(*number):
    total = number[0]   
    for num in number[1:]:
        total /= num
    return total