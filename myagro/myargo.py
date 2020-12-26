def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    sub_li = [[D1, R1], [D2, R2], [D3, R3]]
    sub_li.sort(key=lambda x: x[0])
    # print(sub_li)
    index = -1
    Power = 0
    while True:
        index += 1
        # print(f'Day {index} started')
        if (index >= sub_li[0][0]) and (index < sub_li[1][0]):
            K -= sub_li[0][1]
            # print(f'{K}-1')
            Power += 1
            if (K < sub_li[0][1]):
                break
        elif (index >= sub_li[1][0]) and (index < sub_li[2][0]):
            K -= (sub_li[0][1]+sub_li[1][1])
            # print(f'{K}-2')
            Power += 1
            if (K < (sub_li[0][1] + sub_li[1][1])):
                break
        elif (index >= sub_li[2][0]):
            K -= (sub_li[0][1]+sub_li[1][1]+sub_li[2][1])
            # print(f'{K}-3')
            Power += 1
            if (K < (sub_li[0][1] + sub_li[1][1] + sub_li[2][1])):
                break
    return Power


# get_days_of_power(
#     R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
