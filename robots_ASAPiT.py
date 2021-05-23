length = 20
count = 7
robots = list(map(int, input().split()))
mid = length // 2
m_l = -1
for robot in robots:
    if robot <= mid:
        ch = length - robot
    else:
        ch = robot

    if ch > m_l:
        m_l = ch

print(m_l)