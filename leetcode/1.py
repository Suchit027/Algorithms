def isfence(alice, bob):
    if alice[0] <= bob[0] and alice[1] >= bob[1]:
        return True
    return False


def numberOfPairs(points):
    length = len(points)
    ans = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if isfence(points[i], points[j]):
                flag = True
                for x in points:
                    if x == points[i] or x == points[j]:
                        continue
                    if points[i][0] <= x[0] <= points[j][0] and points[i][1] >= x[1] >= points[j][1]:
                        flag = False
                        break
                if flag:
                    ans += 1
    return ans


if __name__ == '__main__':
    points = [[6, 2], [4, 4], [2, 6]]
    print(numberOfPairs(points))
