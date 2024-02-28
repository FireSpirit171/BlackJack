from tkinter import *
from tkinter import ttk
import random
from copy import deepcopy
from PIL import Image, ImageTk
from logic import total
from read import read_singletone
from config_path import ICON_PATH, STAT_PATH, CARD_PATH, CROUPIER_PATH, RULE

#/////////////////////////////ВЗЯТО ИЗ LOGIC.PY//////////////////////////
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
#///////////////////////////////////////////////////////////////////////////////


def finish():
    global widget
    widget.destroy()

def rules():
    global widget
    for w in widget.winfo_children():
        w.destroy()

    rule = Text(background="green", foreground="white", font=("Arial", 14), wrap="word")
    ys = ttk.Scrollbar(orient="vertical", command=rule.yview)
    
    rule.place(height=400, width=700, x=100, y=100)
    rule.insert("1.0", RULE)
    
    ys.pack(side=RIGHT, fill=Y)
    rule["yscrollcommand"] = ys.set

    back_button = ttk.Button(widget, text="Назад", command=exit_game)
    back_button.place(x=0, y=0)

def rewrite_stat():
    with open (STAT_PATH, 'w') as stat_file:
        stat_file.write("Games: 0\n")
        stat_file.write("Wons: 0\n")
        stat_file.write("Draws: 0\n")
        stat_file.write("Loses: 0\n")
        stat_file.write("Percant: 0")

        
def show_stat():
    global widget, stat_file
    games, wons, draws, loses, percent = stat_file.read_file()
    
    for w in widget.winfo_children():
        w.destroy()

    #Фрейм статистики и лэйблы
    stat_frame = ttk.Frame(borderwidth=1, relief=SOLID)
    games_label = ttk.Label(stat_frame, text=f"Количество игр: {games}", background="green", foreground="white", font=("Arial", 16))
    wons_label = ttk.Label(stat_frame, text=f"Победы: {wons}", background="green", foreground="white", font=("Arial", 16))
    draws_label = ttk.Label(stat_frame, text=f"Ничьи: {draws}", background="green", foreground="white", font=("Arial", 16))
    loses_label = ttk.Label(stat_frame, text=f"Поражения: {loses}", background="green", foreground="white", font=("Arial", 16))
    percent_label = ttk.Label(stat_frame, text=f"Процент побед: {percent}%", background="green", foreground="white", font=("Arial", 16))
    
    games_label.pack(fill=X, ipadx=10, ipady=10)
    wons_label.pack(fill=X, ipadx=10, ipady=10)
    draws_label.pack(fill=X, ipadx=10, ipady=10)
    loses_label.pack(fill=X, ipadx=10, ipady=10)
    percent_label.pack(fill=X, ipadx=10, ipady=10)

    stat_frame.pack(expand=True)

    back_button = ttk.Button(widget, text="Назад", command=exit_game)
    back_button.place(x=0, y=0)

def start_game():
    global widget
    hide_widgets()
    game()

def hide_widgets():
    global widget
    for child_widget in widget.winfo_children():
        child_widget.destroy()

def show_widgets():
    global widget
    for child_widget in widget.winfo_children():
        child_widget.pack()

def exit_game():
    global widget
    for w in widget.winfo_children():
        w.destroy()
    main()

all_images = []
num_cards_on_screen = 0
def show_card(path, X, Y = 480):
    global widget
    global all_images
    global num_cards_on_screen
    image_file = Image.open(path)
    vp_image = ImageTk.PhotoImage(image_file)
    all_images.append(vp_image)

    label = Label(image=all_images[num_cards_on_screen])
    num_cards_on_screen += 1
    label.place(x=X, y=Y)
    #widget.update()
    #widget.update_idletasks()

def take_card(player, cards):
    global widget, stat_file
    player.append(cards[0])

    show_card(CARD_PATH.format(cards.pop(0)), 240+len(player)*80)

    player_tot = total(player)
    score = ttk.Label(widget, text=f"Сумма: {player_tot}", background="green", foreground="white", font=("Arial", 14))
    score.place(height=40, width=100, x=10, y=520)

    if player_tot>21:
        stat_file.update_stat(-1)
        for w in widget.winfo_children():
            if type(w)==ttk.Button:
                w.destroy()
        end = ttk.Label(widget, text="Вы проиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
        menu_button = ttk.Button(text="Меню", command=main)
        new_game_button = ttk.Button(text="Новая игра", command=start_game)
        
        menu_button.place(height=50, width=120, x=340, y=330)
        new_game_button.place(height=50, width=120, x=470, y=330)

def croupier_take(croupie, cards, player):
    global widget, stat_file
    show_card(CARD_PATH.format(croupie[1]), 400, 150)
    player_tot = total(player)
    for w in widget.winfo_children():
        if type(w)==ttk.Button:
            w.destroy()

    croupie_tot = total(croupie)

    while croupie_tot<17:
        croupie.append(cards[0])
        show_card(CARD_PATH.format(cards.pop(0)), 240+len(croupie)*80, 150)
        croupie_tot = total(croupie)

    #После добора крупье считаем победителя
    if croupie_tot>21 or croupie_tot<player_tot:
        stat_file.update_stat(1)
        end = ttk.Label(widget, text="Вы выиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    elif croupie_tot==player_tot:
        stat_file.update_stat(0)
        end = ttk.Label(widget, text="Ничья!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    else:
        stat_file.update_stat(-1)
        end = ttk.Label(widget, text="Вы проиграли!", background="green", foreground="white", font=("Arial", 24))
        end.place(height=90, width=240, x=350, y=250)
    
    #Кнопки возврата в меню или начала новой игры
    menu_button = ttk.Button(text="Меню", command=main)
    new_game_button = ttk.Button(text="Новая игра", command=start_game)
    menu_button.place(height=50, width=120, x=340, y=330)
    new_game_button.place(height=50, width=120, x=470, y=330)


def game():
    
    global all_images
    global num_cards_on_screen
    all_images.clear()      #Очистка буфера после предыдущей игры
    num_cards_on_screen=0   #Очистка буфера после предыдущей игры
    X = 320
    Y = 480

    #Фото крупье
    croupier_file = Image.open(CROUPIER_PATH)
    vp_croupier = ImageTk.PhotoImage(croupier_file)
    all_images.append(vp_croupier)
    croupier_label = Label(background="green", image=all_images[num_cards_on_screen])
    num_cards_on_screen += 1
    croupier_label.place(height=120, width=140, x=350, y=10)

    #Выход из игры
    back_button = ttk.Button(widget, text="Выйти из игры", command=exit_game)
    back_button.pack(anchor='nw')
    
    #Тасовка карт
    random.shuffle(all_cards)
    cards = deepcopy(all_cards)

    #Раздаем начальные карты
    player = [cards[0], cards[1]]
    croupier = [cards[2], cards[3]]
    for i in range(4):
        cards.pop(0)
    
    player_tot = total(player)

    #Показываем начальные карты
    show_card(CARD_PATH.format(player[0]), X, Y)
    show_card(CARD_PATH.format(player[1]), X+80, Y)
    
    show_card(CARD_PATH.format(croupier[0]), X, 150)
    show_card(CARD_PATH.format("back"), X+80, 150)

    #Счет
    score = ttk.Label(widget, text=f"Сумма: {player_tot}", background="green", foreground="white", font=("Arial", 14))
    score.place(height=40, width=100, x=10, y=520)

    #Передаем ход игроку
    new_card_button = ttk.Button(widget, text="Ещё!", command=lambda pl = player, cs = cards: take_card(pl, cs))
    new_card_button.place(x=400, y=450)

    #Передаем ход крупье
    stop_card_button = ttk.Button(widget, text="Хватит", command=lambda cr = croupier, cs = cards, pl = player: croupier_take(cr, cs, pl))
    stop_card_button.place(x=500, y=450)


def main():
    for w in widget.winfo_children():
        w.destroy()

    #Управление на главном окне
    frame_main = ttk.Frame(borderwidth=1, relief=SOLID)
    button_start = ttk.Button(frame_main, text="Новая игра", command = start_game, width=50)
    button_continue = ttk.Button(frame_main, text="Правила", command=rules, width=50)
    button_stat = ttk.Button(frame_main, text="Статистика", command = show_stat, width=50)
    button_start.pack(fill=X, ipadx=10, ipady=10)
    button_continue.pack(fill=X, ipadx=10, ipady=10)
    button_stat.pack(fill=X, ipadx=10, ipady=10)

    #frame_main.place(x=300, y=232, height=136, width=300)
    frame_main.pack(expand=True)

    widget.mainloop()
    #widget.protocol("WM_DELETE__WINDOW", finish)


if __name__ == "__main__":
    widget = Tk()
    widget["bg"] = "green"
    widget.resizable(False, False)
    widget.title("BlackJack")
    icon = PhotoImage(file=ICON_PATH)
    widget.iconphoto(False, icon)
    widget.geometry("900x600+300+100")
    rewrite_stat()
    stat_file = read_singletone(STAT_PATH) #Переменная для работы со статистикой
    main()
