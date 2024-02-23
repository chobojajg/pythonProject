import random
import sys

before_battle = []
com_rsp_dic: dict = {1: 'r', 2: 's', 3: 'p'}
player_rsp_list = ['가위', '바위', '보', 'rock', 'paper', 'scissors', 'r', 's', 'p']

while(True):
    random_num = random.randint(1, 3)
    com_rsp = com_rsp_dic[random_num]

    while(True):
        player_rsp = input('가위, 바위, 보 중 하나를 선택하세요: ').lower()

        if player_rsp == 'end':
            sys.exit()

        if player_rsp == ('가위' or 'scissors' or 's'):
            player_rsp = 's'
        elif player_rsp == ('바위' or 'rock' or 'r'):
            player_rsp = 'r'
        elif player_rsp == ('보' or 'paper' or 'p'):
            player_rsp = 'p'

        if player_rsp not in player_rsp_list:
            print('유효한 입력이 아닙니다.')
        elif com_rsp == player_rsp:
            print('비겼습니다!')
            before_battle.append('d')
            break
        elif com_rsp == 'r':
            if player_rsp == 's':
                print('컴퓨터 승리!')
                before_battle.append('l')
                break
            elif player_rsp == 'p':
                print('사용자 승리!')
                before_battle.append('w')
                break
        elif com_rsp == 's':
            if player_rsp == 'p':
                print('컴퓨터 승리!')
                before_battle.append('l')
                break
            elif player_rsp == 'r':
                print('사용자 승리!')
                before_battle.append('w')
                break
        elif com_rsp == 'p':
            if player_rsp == 'r':
                print('컴퓨터 승리!')
                before_battle.append('l')
                break
            elif player_rsp == 's':
                print('사용자 승리!')
                before_battle.append('w')
                break

    while (True):
        re_play_check = input('다시 하시겠습니까? (y/n): ')

        if re_play_check == 'y':
            break
        elif re_play_check == 'n':
            print('게임을 종료합니다')
            print(f'승: {before_battle.count('w')} 패: {before_battle.count('l')} 무: {before_battle.count('d')}')
            sys.exit()
        else:
            print("y나 n을 입력해주세요")
