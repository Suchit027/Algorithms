def knapsack(weight_list):
    people = len(weight_list)
    dp = [[0 for x in range(people + 1)] for y in range(people + 1)]

