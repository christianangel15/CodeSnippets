def compute_number_score(number):
    score = 0
    if (number % 3 == 0):
        score = score + 4
    elif (number % 2 == 0) or (number == 0):
        score = score + 3
    num = [x for x in str(number)]
    num.sort()
    tp = []
    for i in num:
        if (i == '7'):
            score = score + 5
        elif (i == '2'):
            tp.append(i)
            if len(tp) > 1:
                score = score + 6

    print(score)


compute_number_score(2067)
