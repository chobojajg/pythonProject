import random
import sys

before_cnt = []

while(True):
    random_num = random.randint(1, 100)
    try_cnt = 0

    print('-------------------------------')
    print('업다운 게임에 오신걸 환영합니다')
    print('1에서 100 사이의 숫자를 맞춰보세요')
    print('-------------------------------')

    if len(before_cnt) > 0:
        print("이전 게임 플레이어 최고 시도 횟수: " + str(min(before_cnt)))
        print('-------------------------------')

    while(True):
        user_num = input("숫자를 입력하세요: ")

        if user_num == 'end':
            sys.exit()

        try:
            if int(user_num) > 100 or int(user_num) < 1:
                print("숫자는 1에서 100사이의 숫자를 입력해 주세요")
            elif int(user_num) == random_num:
                try_cnt += 1
                print('맞았습니다')
                break
            elif int(user_num) > random_num:
                try_cnt += 1
                print('다운')
            elif int(user_num) < random_num:
                try_cnt += 1
                print('업')
        except Exception as e:
            print("숫자를 입력해 주세요")

    print('시도한 횟수: ' + str(try_cnt))
    before_cnt.append(try_cnt)

    while(True):
        re_play_check = input('다시 하시겠습니까? (y/n): ')

        if re_play_check == 'y':
            break
        elif re_play_check == 'n':
            print('게임을 종료합니다')
            sys.exit()
        else:
            print("y나 n을 입력해주세요")