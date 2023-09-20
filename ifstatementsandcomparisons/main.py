def max_num(nnum1 , num2 , num3):
    if nnum1 >= num2 and nnum1 >= num3:
        return nnum1
    elif num2 >= num3 and num2 >= nnum1:
        return num2
    elif num3 >= nnum1 and num3 >= num2:
        return num3
    else:
        return num3

print(max_num(314 , 52 , 84))