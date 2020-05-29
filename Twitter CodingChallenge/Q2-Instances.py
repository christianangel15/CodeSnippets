import math
def finalInstances(instances, averageUtil):
    UtilIter = iter(averageUtil)
    for ele in UtilIter:
        if [ele] > [60] and instances*2 < 2*10^8:
            instances = instances*2
            for _ in range(10):
                next(UtilIter, None)
        elif [ele] < [25] and instances/2 >= 1:
            instances = math.ceil(instances/2)
            for _ in range(10):
                next(UtilIter, None)
    return instances
Inst = finalInstances(1,3,5,10,80)
print(Inst)
