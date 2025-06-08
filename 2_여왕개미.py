Q = int(input())

house_list = [0]
broken_list = [False]

def buildCountry(commands):
    global house_list, broken_list

    N = commands[0]
    for house in commands[1:]:
        house_list.append(house)
        broken_list.append(False)

def buildHouse(p):
    global house_list
    house_list.append(p)
    broken_list.append(False)

def removeHouse(q):
    global house_list, broken_list
    broken_list[q] = True

def search(r):
    global house_list, broken_list

    lowerbound, upperbound = 0, 1e+9
    minTime = 0

    while lowerbound <= upperbound:
        midTime = (lowerbound+upperbound)//2
        ant_cover_cnt = 0
        last_pos = -1e+9

        for i in range(1, len(house_list)):
            # 안전하거나 폐가인 경우 skip ~
            if broken_list[i]:
                continue
            
            current_pos = house_list[i]

            # 이전 위치에서 현재 위치까지 도달하는 데에 제안된 시간보다 더 걸린다면 (지금 있는 개미로 못가는 경우)
            if current_pos - last_pos > midTime:
                # 현재 위치에서 정찰 시작
                last_pos = current_pos
                # 새 개미 필요
                ant_cover_cnt += 1
        # 개미수가 제시된 r 이하인지 체크하는 부분 
        if ant_cover_cnt <= r:
            minTime = midTime
            upperbound = midTime -1
        else:
            lowerbound = midTime + 1
    #여왕에거 시간 보고
    print(int(minTime))


for _ in range(Q):
    commands = list(map(int, input().split()))

    if commands[0] == 100: #마을건설
        buildCountry(commands[1:])
        # print(100, house_list, broken_list)

    elif commands[0] == 200: #개미집건설
        buildHouse(commands[1])
        # print(200, house_list, broken_list)

    elif commands[0]==300: #개미집철거
        removeHouse(commands[1])
        # print(300, house_list, broken_list)

    elif commands[0]==400:
        search(commands[1])
        # print(400, house_list, broken_list)

    else:
        print("the command input is wrong")

