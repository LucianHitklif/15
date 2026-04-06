print ("""Символы в лабиринте:
    0 — проход (можно идти)
    1 — стена (нельзя пройти)
    л — ловушка (-10 HP)
    м — монета (+1 монета)
    ф — выход (нужно дойти до него и не погибнуть)
    з — враг (-50 HP)
    н — начальная точка (вход)
    """)
maze = input('Введите строку лабиринта (25 символов): ')
if len(maze) != 25:
    print('Строка должна содержать 25 символов!')
else:
    for row in range(5):
        start = row * 5
        end = start + 5
        print(maze[start:end])

    if 'н' not in maze:
        print("Вход не найден")
    elif 'ф' not in maze:
        print("Выход не найден")
    else:
        st_ind = maze.index('н')
        st_row = st_ind // 5
        st_col = st_ind % 5
        ex_ind = maze.index('ф')
        ex_row = ex_ind // 5
        ex_col = ex_ind % 5
        print(f"""Координаты входа (н): строка {st_row}, столбец {st_col}
Координаты выхода (ф): строка {ex_row}, столбец {ex_col}""")

        dist = abs(st_row - ex_row) + abs(st_col - ex_col)
        print(f"Манхэттенское расстояние: {dist}")

    сoin_count = maze.count('м')
    if сoin_count >0:
        print(f'Монет: 🪙 x {сoin_count}')
    else:
        print('Монет нет')

    hp = 100
    trap_count = maze.count('л')
    enemy_count = maze.count('з')
    print(f"Ловушек: {trap_count}")
    print(f'Врагов: {enemy_count}')
    damage = (trap_count*10) + (enemy_count*50)
    rem_hp = hp - damage
    print(f"""Полученный урон: {damage}
Оставшееся здоровье: {rem_hp}""")
    full_heart = rem_hp //10
    lost_heart = damage // 10
    hearts = '♥' * full_heart + '♡' * lost_heart
    print(hearts)
