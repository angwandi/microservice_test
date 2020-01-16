# Grading Students
def grading_students(grades):
    for i in range(len(grades)):
        if grades[i] > 37:
            if (grades[i] % 5) != 0:
                if 5 - (grades[i] % 5) < 3:
                    grades[i] += 5 - (grades[i] % 5)
    return grades


# Counting Valleys
def counting_valleys(n, s):
    level = valley = 0
    for i in range(n):
        if s[i] == 'U':
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1
    return valley


# Sock Merchant
def sock_merchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i < n:
        if ar[i] == ar[i + 1]:
            count = count + 1
            i += 2
        else:
            i += 1
    return count
