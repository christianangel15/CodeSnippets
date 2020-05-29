def canReach(x1, y1, x2, y2):
    if (x1 < x2) and (y1 < y2) and (x2 - x1) == y1:
            return 'Yes'
    else:
        return 'No'
i=canReach(1,4,5,9)
print(i)
