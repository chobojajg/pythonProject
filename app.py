
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_history = []
before_battle = []
com_rsp_dic: dict = {1: 'r', 2: 's', 3: 'p'}

@app.route('/')
def home():
    random_num = random.randint(1, 3)
    com_rsp = com_rsp_dic[random_num]

    query = request.args.get('query')

    # com_rsp:컴퓨터,player_rsp:사람,승패 순서
    # r:바위, s:가위, p:보, w:사람 승리, l:사람 패배, d:비김
    def rsp_game(player_rsp):
        if com_rsp == player_rsp:
            print('비겼습니다!')
            result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'd'}
            return all_history.append(result), before_battle.append('d')
        elif com_rsp == 'r':
            if player_rsp == 's':
                print('컴퓨터 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'l'}
                return all_history.append(result), before_battle.append('l')
            elif player_rsp == 'p':
                print('사용자 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'w'}
                return all_history.append(result), before_battle.append('w')
        elif com_rsp == 's':
            if player_rsp == 'p':
                print('컴퓨터 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'l'}
                return all_history.append(result), before_battle.append('l')
            elif player_rsp == 'r':
                print('사용자 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'w'}
                return all_history.append(result), before_battle.append('w')
        elif com_rsp == 'p':
            if player_rsp == 'r':
                print('컴퓨터 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'l'}
                return all_history.append(result), before_battle.append('l')
            elif player_rsp == 's':
                print('사용자 승리!')
                result = {"com_rsp": com_rsp, 'player_rsp': player_rsp, 'wol': 'w'}
                return all_history.append(result), before_battle.append('w')

    rsp_game(query)

    print(f'승: {before_battle.count('w')} 패: {before_battle.count('l')} 무: {before_battle.count('d')}')

    count_list = {'win': before_battle.count('w'), 'lose': before_battle.count('l'), 'draw': before_battle.count('d')}

    return render_template('index.html', all_history=all_history, count_list=count_list)

    # return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)