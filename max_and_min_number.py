def max_and_min(num=[]):
    output = []
    num.sort()
    minimum= num[len(num)-1]
    maximum = num[0]

    output.append(minimum)
    output.append(maximum)
    if minimum == maximum:
        output.pop(0)

    return output