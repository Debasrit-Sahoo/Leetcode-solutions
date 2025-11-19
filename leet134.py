def canCompleteCircuit(gas, cost):
        start = 0
        tank = 0
        tgas, tcost = 0, 0
        for i in range(len(gas)):
            tgas += gas[i]
            tcost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        if tgas >= tcost:
            return start
        return -1