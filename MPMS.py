import hashlib
import sys


class Member:
    name = ''
    username = ''
    password = ''

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'아이디: {self.username}, 유저이름: {self.name}')


class Post:
    title = ''
    content = ''
    author = ''
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 메인 메뉴
def main_menu(members, login_data, posts):
    print(members)
    print(login_data)
    print(posts)
    print('----------------------------------------')
    print('사용하시려는 기능의 번호를 입력해 주세요')
    print('1. 로그인')
    print('2. 회원가입')
    print('3. 종료')
    print('----------------------------------------')
    choice_main = input('')

    if choice_main == '1':  # 로그인
        return login_user(members, login_data, posts)
    elif choice_main == '2':  # 회원가입
        return input_user(members, login_data, posts)
    elif choice_main == '3':
        sys.exit()
    else:
        print('없는 기능입니다. 다시 선택해 주세요')
        return main_menu(members, login_data, posts)


# 회원가입
def input_user(members, login_data, posts):
    print('사용하실 아이디와 비밀번호를 입력해 주세요')
    while (True):
        new_id = input('아이디: ')
        if new_id in members:
            print('이미 있는 사용자 입니다.')
            continue
        new_password = input('비밀번호: ')
        hash_object = hashlib.sha256(new_password.encode())
        hex_dig = hash_object.hexdigest()
        new_name = input('이름을 입력해 주세요: ')

        members[new_id] = Member(new_name, new_id, hex_dig)
        members[new_id].display()
        print('회원가입이 완료되었습니다!')
        break

    return main_menu(members, login_data, posts)


# 로그인
def login_user(members, login_data, posts):
    print('아이디와 비밀번호를 입력해 주세요')
    id = input('아이디: ')
    password = input('비밀번호: ')
    hash_object = hashlib.sha256(password.encode())
    password = hash_object.hexdigest()

    if id in members.keys():
        if members[id].password == password:
            print(f'어서오세요 {members[id].name}님!')
            login_data = members[id]
            return user_page(members, login_data, posts)
        else:
            print('아이디 혹은 비밀번호가 틀렸습니다')
            print('비밀번호')
            return login_user(members, login_data, posts)
    else:
        print('아이디 혹은 비밀번호가 틀렸습니다')
        print('아이디')
        return login_user(members, login_data, posts)


# 유저 페이지
def user_page(members, login_data, posts):
    print('----------------------------------------')
    print('원하시는 작업을 선택해 주세요')
    print('1. 게시글 보기')
    print('2. 게시글 작성')
    print('3. 내가 쓴글 보기')
    print('4. 내 정보 수정 - 아직 기능 없음')
    print('5. 로그아웃')
    if login_data.username == 'admin00001':
        print('6. 관리자 기능')
    print('----------------------------------------')

    choice_user_page = input('')

    if choice_user_page == '1':  # 게시글 보기
        return posting_list(members, login_data, posts)
    elif choice_user_page == '2':  # 게시글 작성
        return posting_page(members, login_data, posts)
    elif choice_user_page == '3':  # 내가 쓴글 보기
        return posting_list(members, login_data, posts, login_data.username)
    elif choice_user_page == '4':  # 내 정보 수정
        pass
    elif choice_user_page == '5':  # 로그아웃
        login_data = []
        return main_menu(members, login_data, posts)
    elif choice_user_page == '6' and login_data.username == 'admin00001':  # 관리자 기능
        admin_func(members, login_data, posts)
    else:
        print('없는 기능입니다. 다시 선택해 주세요')
        user_page(members, login_data, posts)


# 게시글 목록
def posting_list(members, login_data, posts, keyword = None):
    print('----------------------------------------')
    print('보고싶은 게시물의 번호를 입력해 주세요')
    print('----------------------------------------')
    for i, post in enumerate(posts):
        if keyword is not None:
            if post.author == login_data.username:
                print(f'{i}.{post.title}')
                continue
            else:
                continue
        print(f'{i}.{post.title}')
    print('----------------------------------------')
    print('"뒤로" 입력 시 유저 페이지로 돌아감')
    choice_posting_list = input()

    if choice_posting_list == '뒤로':
        return user_page(members, login_data, posts)
    try:
        choice_num = int(choice_posting_list)
        try:
            print(f'제목: {posts[choice_num].title}')
            print(f'글쓴이: {posts[choice_num].author}')
            print('내용')
            print(posts[choice_num].content)
            print('')
            print('아무 글자 입력시 나가기')
            out = input()
            if out is not None:
                return posting_list(members, login_data, posts, keyword)
        except:
            print('리스트에 없습니다')
            return posting_list(members, login_data, posts, keyword)
    except:
        print('숫자를 입력해 주세요')
        return posting_list(members, login_data, posts, keyword)


# 게시글 작성
def posting_page(members, login_data, posts):
    post_title = ''
    post_content = ''
    while(True):
        print('----------------------------------------')
        print('쓰고싶은 부분을 선택해 주세요')
        print('제목')
        print('내용')
        print('저장하기')
        print('----------------------------------------')
        select_input = input()
        if select_input == '제목':
            post_title = posting_page_title()
        elif select_input == '내용':
            post_content = posting_page_content()
        elif select_input == '저장하기':
            choice = input('저장하시겠습니까? y/n')
            if choice == 'y':
                posts.append(Post(post_title, post_content, login_data.username))
                break
            elif choice == 'n':
                pass
            else:
                print('원하는 기능을 정확하게 적어주세요')
        else:
            print('원하는 기능을 정확하게 적어주세요')

    return user_page(members, login_data, posts)


# 게시글 작성 제목
def posting_page_title():
    print('----------------------------------------')
    print('쓸 게시글의 제목을 적어주세요')
    print('----------------------------------------')
    post_title = input()
    return post_title


# 게시글 작성 내용
def posting_page_content():
    print('----------------------------------------')
    print('쓸 게시글의 내용을 적어주세요')
    print('----------------------------------------')
    post_content = input()
    return post_content


# 관리자 기능
def admin_func(members, login_data, posts):
    print('----------------------------------------')
    print('원하시는 작업을 선택해 주세요')
    print('1. 게시글 보기')
    print('2. 유저 목록 보기')
    print('3. 로그아웃')
    print('----------------------------------------')
    choice_admin = input()

    if choice_admin == '1':
        return posting_list(members, login_data, posts)
    elif choice_admin == '2':
        return show_user_list_admin(members, login_data, posts)
    elif choice_admin == '3':
        login_data = []
        return main_menu(members, login_data, posts)
    else:
        print('없는 기능입니다. 다시 선택해 주세요')
        admin_func(members, login_data, posts)


# 관리자 기능 - 유저 목록
def show_user_list_admin(members, login_data, posts):
    for i in members:
        if members[i].username == 'admin00001':
            continue
        members[i].display()
    return admin_func(members, login_data, posts)


def back_main():
    while (True):
        re_play_check = input('메인으로 돌아가시겠습니까? (y/n): ')

        if re_play_check == 'y':
            main_menu(members, login_data, posts)
        elif re_play_check == 'n':
            print('프로그램을 종료합니다')
            sys.exit()
        else:
            print("y나 n을 입력해주세요")


members = {}
login_data = []
posts = []

# 관리자 아이디 및 비밀번호
admin_id = 'admin00001'
admin_password = '15951'
admin_name = '나'
hash_object = hashlib.sha256(admin_password.encode())
hex_dig = hash_object.hexdigest()
members[admin_id] = Member(admin_name,admin_id,hex_dig)

# 테스트용 아이디 및 게시글들
test_password = '111'
hash_object = hashlib.sha256(test_password.encode())
hex_dig = hash_object.hexdigest()
members['1'] = Member('11','1',hex_dig)
test_password = '222'
hash_object = hashlib.sha256(test_password.encode())
hex_dig = hash_object.hexdigest()
members['2'] = Member('22','2',hex_dig)
test_password = '333'
hash_object = hashlib.sha256(test_password.encode())
hex_dig = hash_object.hexdigest()
members['3'] = Member('33','3',hex_dig)

posts.append(Post('아', '자고싶다', '1'))
posts.append(Post('어', '망한거 같은데', '1'))
posts.append(Post('음', '이렇게 하는게 맞나', '2'))
posts.append(Post('코드', '산으로 간거 같은데', '3'))

main_menu(members, login_data, posts)
