#exponent function

def exponent_function(base_num,power_num):
    result = 1
    for power in range(power_num):
        result = result * base_num

    return result

print(exponent_function(5,2))