#def getBattery(events):
#    charging = 50
#    eve = list(events)
#    for i in eve:
#        charging = charging + i
#        if charging > 100:
#            charging = 100
#    print(charging)
#getBattery((25, -30, 70, -10))
#---------------------------------------
#def getMinCost(employee_id, job_id):
#    Emp = sorted(employee_id)
#    job = sorted(job_id)
#    travel = []
#    for i in range(len(job)):
#        if Emp[i] > job[i]:
#            tr = [Emp[i] - job[i]]
#            print(tr)
#            travel.extend(tr)
#        else:
#            tr = [job[i] - Emp[i]]
#            print(tr)
#            travel.extend(tr)
#    print (sum(travel))
#getMinCost([5, 3, 1, 4, 6], [9, 8, 3, 15, 1])
