import random


class Vocabulary:
    def __init__(self):
        self.voca = {}
        for i in range(0, int(input('입력할 단어의 개수 : '))):
            print()
            self.voca[input('뜻를 입력하세요 : ')] = input('단어을 입력하세요 : ')
        print()

        self.meanings = []
        self.words = []
        self.correct = 0
        self.wrong = 0

    def set_data(self):
        self.meanings = list(self.voca.keys())
        self.words = list(self.voca.values())
        self.correct = 0
        self.wrong = 0

    def word_game(self):
        for question in random.sample(self.meanings, len(self.words)):
            answer = input(question + ' : ')
            if self.voca[question] == answer:
                print('정답 !!\n')
                self.correct += 1
            else:
                print('오답...\n')
                self.wrong += 1

    def meaning_game(self):
        for question in random.sample(self.words, len(self.words)):
            answer = input(question + ' : ')
            if self.voca[answer] == question:
                print('정답 !!\n')
                self.correct += 1
            else:
                print('오답...\n')
                self.words += 1

    def print_voca(self):
        print('-'*30)
        for i in range(0, len(self.words)):
            print(f'{i+1}. {self.words[i]} : {self.meanings[i]}')
        print('-'*30)

    def add_word(self):
        for i in range(0, int(input('입력할 단어의 개수 : '))):
            print()
            self.voca[input('뜻를 입력하세요 : ')] = input('단어을 입력하세요 : ')
        print()

    def del_word(self):
        del self.voca[input('삭제할 단어의 뜻을 입력하세요 : ')]

    def total(self):
        print('-'*10 + '총점' + '-'*10)
        print(f'맞은 개수 : {self.correct}')
        print(f'틀린 개수 : {self.wrong}')
        print('-'*22)


def index_for_main():
    print('-'*11 + '영어 단어장' + '-'*11)
    print('\t1. 단어장 선택하기')
    print('\t2. 단어장 생성하기')
    print('\t3. 단어장 삭제하기')
    print('-'*33)


def index_for_voca():
    print('-' * 30)
    print('\t1. 단어 맞추기')
    print('\t2. 뜻 맞추기')
    print('\t3. 단어장 출력하기')
    print('\t4. 단어 추가하기')
    print('\t5. 단어 삭제하기')
    print('-' * 30)


if __name__ == '__main__':
    voca_list = []
    while True:
        index_for_main()
        key = input('선택할 숫자를 입력하세요(Q:종료) : ')
        if key == '1':
            voca_num = int(input('단어장의 번호를 입력하세요 : ')) - 1
            if 0 <= voca_num < len(voca_list):
                while True:
                    index_for_voca()
                    option = input('선택할 숫자를 입력하세요(Q:종료) : ')
                    if option == '1':
                        voca_list[voca_num].set_data()
                        voca_list[voca_num].word_game()
                        voca_list[voca_num].total()
                    elif option == '2':
                        voca_list[voca_num].set_data()
                        voca_list[voca_num].meaning_game()
                        voca_list[voca_num].total()
                    elif option == '3':
                        voca_list[voca_num].set_data()
                        voca_list[voca_num].print_voca()
                    elif option == '4':
                        voca_list[voca_num].add_word()
                    elif option == '5':
                        voca_list[voca_num].del_word()
                    elif option == 'Q' or option == 'q':
                        break
                    else:
                        print(f'{int(option)}번 기능은 존재하지 않습니다.')
            else:
                print(f'{voca_num + 1}번 단어장은 존재하지 않습니다.')

        elif key == '2':
            print(f'{len(voca_list)+1}번째 단어장을 생성합니다.')
            voca_list.append(Vocabulary())

        elif key == '3':
            del_index = int(input('삭제할 단어장의 번호를 입력하세요 : ')) - 1
            if 0 <= del_index < len(voca_list):
                del voca_list[del_index]
                print(f'{del_index + 1}번 단어장이 삭제되었습니다.')
            else:
                print(f'{del_index + 1}번 단어장은 존재하지 않습니다.')

        elif key == 'Q' or key == 'q':
            print('프로그램을 종료합니다.')
            break

        else:
            print(f'{key}번 기능은 존재하지 않습니다.')
