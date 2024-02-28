#//////////////////РЕАЛИЗАЦИЯ ЛОГИКИ ИГРЫ В BLACKJACK/////////////////////////
import random
from copy import deepcopy

#Все карты и их значения
hearts = {
    "2_h": 2,
    "3_h": 3,
    "4_h": 4,
    "5_h": 5,
    "6_h": 6,
    "7_h": 7,
    "8_h": 8,
    "9_h": 9,
    "10_h": 10,
    "J_h": 10,
    "Q_h": 10,
    "K_h": 10,
    "A_h": 11 
}

diamonds = {
    "2_d": 2,
    "3_d": 3,
    "4_d": 4,
    "5_d": 5,
    "6_d": 6,
    "7_d": 7,
    "8_d": 8,
    "9_d": 9,
    "10_d": 10,
    "J_d": 10,
    "Q_d": 10,
    "K_d": 10,
    "A_d": 11 
}

spades = {
    "2_s": 2,
    "3_s": 3,
    "4_s": 4,
    "5_s": 5,
    "6_s": 6,
    "7_s": 7,
    "8_s": 8,
    "9_s": 9,
    "10_s": 10,
    "J_s": 10,
    "Q_s": 10,
    "K_s": 10,
    "A_s": 11 
}

clubs = {
    "2_c": 2,
    "3_c": 3,
    "4_c": 4,
    "5_c": 5,
    "6_c": 6,
    "7_c": 7,
    "8_c": 8,
    "9_c": 9,
    "10_c": 10,
    "J_c": 10,
    "Q_c": 10,
    "K_c": 10,
    "A_c": 11 
}

#Информация о всех картах
info = {}
info.update(hearts)
info.update(diamonds)
info.update(clubs)
info.update(spades)

#Непосредственно сами карты
all_cards = []
for m in [hearts, diamonds, spades, clubs]:
    all_cards.extend(m.keys())

#Подсчет суммы карт
def total(person):
    total_value = 0
    ace_count = 0

    for card in person:
        if card[0] in ['K', 'Q', 'J']:
            total_value += info[card]
        elif card[0] == 'A':
            ace_count += 1
            total_value += info[card]
        else:
            total_value += info[card]

    # Обработка того, что Ace может считаться за 1, если сумма больше 21
    while ace_count > 0 and total_value > 21:
        total_value -= 10
        ace_count -= 1

    return total_value

#Покаазть карты
def show_cards(person, is_player=True):
    print("Ваши карты: " if is_player else "Карты крупье: ", end="")
    for card in person:
        print(card, end=" ")
    print()

#Определение победителя
def get_winner(p, c):
    if p>c:
        print("Вы выиграли")
    elif p==c:
        print("Ничья")
    else:
        print("Вы проиграли")


def player_turn(player, cards):
    #Считаем количество взятых карт
    num = 0
    correct = 0 #Необходима для корректировки значения туза - 1 или 11
    player_tot = total(player)
    show_cards(player)
    print("Сумма: ", player_tot)

    #Добор карт
    print("Взять еще карту? [y/n]")
    ans = input()
    while (ans!='n' and ans!='y'):
        print("Повторите ввод")
        ans = input()
    
    aces = {"A_s", "A_h", "A_c", "A_d"}
    while ans=='y':
        player.append(cards[num])
        num+=1
        player_tot = total(player) - correct
        show_cards(player)

        #Проверка на превышение и возврат индикаторного значения
        if player_tot>21:
            #При превышении туз считается не за 11 а за 1
            double = set(player).intersection(aces)               #Если у игрока есть туз
            if len(double)!=0:                                    #Находим общего туза у игрока и среди всех тузов
                correct += 10                                     #Прибавляем к correct 10 (теперь этот туз не 11 а 1)   
                aces.difference_update(double)                    #Убираем туза из aces
            else:
                return player, player_tot, -1

        player_tot = total(player) - correct
        print("Сумма: ", player_tot)

        print("Взять еще карту? [y/n]")
        ans = input()
        while (ans!='n' and ans!='y'):
            print("Повторите ввод")
            ans = input()
    
    return player, player_tot, num


def croupier_turn(croupie, cards):
    num = 0
    correct = 0 #Необходима для корректировки значения туза - 1 или 11
    croupie_tot = total(croupie)

    aces = {"A_s", "A_h", "A_c", "A_d"}
    while croupie_tot<17:
        croupie.append(cards[num])
        num+=1
        croupie_tot = total(croupie) - correct

        if croupie_tot>21:
            #При превышении туз считается не за 11 а за 1
            double = set(croupie).intersection(aces)      #Если у крупье есть туз
            if len(double)!=0:                                    #Находим общего туза у крупье и среди всех тузов
                correct += 10                             #Прибавляем к correct 10 (теперь этот туз не 11 а 1)   
                aces.difference_update(double)            #Убираем туза из aces
            else:
                return croupie, croupie_tot, -1
        
        croupie_tot = total(croupie) - correct
  
    return croupie, croupie_tot, num

def init_game():
    #Тасовка карт
    random.shuffle(all_cards)
    cards = deepcopy(all_cards)

    # Раздаем начальные карты
    player = [cards[0], cards[1]]
    croupier = [cards[2], cards[3]]
    for i in range(4):
        cards.pop(0)
    
    player_tot = total(player)
    croupier_tot = total(croupier)
    
    return player, croupier, cards, player_tot, croupier_tot

def main():
    player, croupier, cards, player_tot, croupier_tot = init_game()

    #Передаем ход игроку
    player, player_tot, player_took = player_turn(player, cards)
    if player_took ==-1:
        print("Сумма: ", player_tot)
        print("Вы проиграли!")
        return
    
    #Удаляем из колоды карты, которые взял игрок
    for _ in range(player_took):
        cards.pop(0)
    
    #Передаем ход крупье
    croupier, croupier_tot, croupier_took = croupier_turn(croupier, cards)
    if croupier_took == -1:
        print("*************")
        show_cards(player)
        print("Сумма: ", player_tot)
        show_cards(croupier, False)
        print("Сумма: ", croupier_tot)
        print("*************")
        print("Вы выиграли")
        return
    for _ in range(croupier_took):
        cards.pop(0)

    print("*************")
    show_cards(player)
    print("Сумма: ", player_tot)
    show_cards(croupier, False)
    print("Сумма: ", croupier_tot)
    print("*************")

    get_winner(player_tot, croupier_tot)

    


if __name__ == "__main__":
    ans = 'y'
    while ans != 'n':
        main()
        print("Начать новую игру? [y/n]")
        ans = input()
        while (ans!='y' and ans!='n'):
            print("Повторите ввод")
            ans = input()