    # 2.    Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""
import random

def player_tour(max_num, num, player):
    take_sweet = -1
    while 0 > take_sweet or take_sweet > max_num or take_sweet > num:
        take_sweet = int(input(f'Сколько конфет из {num} возмет игрок {player}? '))
        if take_sweet > max_num:
            print(f'Максимально количество конфет которые можно взять -  {max_num}!')
        elif take_sweet > num:
            print(f'Осталось всего {num} кофет!')
        elif take_sweet == 0:
            print(f'Надо взять минимум одну конфету!')
    return take_sweet

def bot_tour(max_num, num):
    if num <= max_num:
        take_sweet = num
    elif num > max_num and num - max_num <= max_num + 1:
        take_sweet = num - max_num - 1
    else:
        take_sweet = num - (num // (max_num + 1)) * (max_num + 1) + 1
    take_sweet = 1 if take_sweet == 0 or take_sweet > max_num else take_sweet
    print(f'Бот берет {take_sweet} конфет(у).')
    return take_sweet    

num_of_sweets = 201
sweet_on_tour = 28
print(f'  На столе лежит {num_of_sweets} конфет(а). Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {sweet_on_tour} конфет. \
Все конфеты оппонента достаются сделавшему последний ход. Если хотите играть с ботом - введите имя "bot".')
p_name = []
p_name.append(input("Имя первого игрока: "))
p_name.append(input("Имя второго игрока: "))

in_game_player = random.randint(0,1)

print(f'Первым ходит игрок {p_name[in_game_player]}')
   
game_sweet = num_of_sweets

while game_sweet > 0:
    if 'bot' not in p_name[in_game_player]:
        game_sweet -= player_tour(sweet_on_tour, game_sweet, p_name[in_game_player])
    else:
        game_sweet -= bot_tour(sweet_on_tour, game_sweet)
    print(f'Осталось конфет - {game_sweet}.')
    in_game_player = int(not bool(in_game_player))
print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')