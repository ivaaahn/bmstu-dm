#!/usr/bin/python3

import numpy as np
from math import inf


GREEN = "\x1b[32m"
RESET = "\x1b[0m"
YELLOW = "\x1b[33m"


# Считываем матрицу
matrix = np.loadtxt('data/dfs_org', dtype=int)
# start = int(input(f'Enter index of start vertex, please [0, {len(matrix[0]) - 1}]: '))

# Размер считанной матрицы
size = len(matrix[0])

# Объявим счетчик вершин
vertex_count = 0

# Начальные установки: множества древесных и обратных дуг пусты
wood_edges = []
back_edges = []
forward_edges = []
cross_edges = []

# !Временно
errors_edges = [] 

# Начальные установки: множество фундаментальных циклов и стек пусты
fund_cycles = []
stack = []

# Дефолтная нумерация вершин для удобства
vertices = [vert for vert in range(size)]

# Т. н. Д-номера, которые получат вершины после обхода
d_numbers = [None for _ in range(size)]

# Метки для новых вершин. Изначально - все новые.
new = [True for _ in range(size)]

# Для самопроверки сформируем массив лидеров со списками смежности
adj_list = []
for i in range(size):
    adj_list.append([j for j in range(size) if matrix[i][j] > 0])


# Основная функция, которая получает на вход очередную вершину
def dfs(v):
    global vertex_count # используем глобальный счетчик

    # Предобработка полученной вершины
    new[v] = False              # помечаем полученную вершину посещенной
    d_numbers[v] = vertex_count # присваиваем полученной вершине номер
    vertex_count += 1           # Увеличиваем счетчик
    stack.append(v)             # Пихаем вершину в стек

    print(YELLOW + f'Стек: {stack}' + RESET)

    # Основная обработка вершины
    # Перебираем все вершины из списка смежности.
    for w in adj_list[v]:
        # Если данную вершину посещаем впервые, то ребро идет в древесное
        # Продолжаем поиск к глубину. Запускаем от текущей вершины
        if new[w]:
            wood_edges.append([v, w])
            print(f'({v}, {w}) -> Древесные')
            dfs(w)
        # Если вершину уже посещали то смотрим на классификацию вершины
        # Если она не классифицирована, то классифицируем.
        elif [v, w] not in wood_edges and [v, w] not in back_edges:

            if d_numbers[v] >= d_numbers[w] and w in stack:
                back_edges.append([v, w])
                print(f'({v}, {w}) -> Обратные')
            elif d_numbers[v] < d_numbers[w]:
                forward_edges.append([v, w])
                print(f'({v}, {w}) -> Прямые')
            elif d_numbers[v] >= d_numbers[w] and w not in stack:
                cross_edges.append([v, w])
                print(f'({v}, {w}) -> Поперечные')
            else:
                errors_edges.append([v, w])
    
    # После окончания обработки списка смежности вершины выкидываем вершину из стека.
    stack.pop()
    print(YELLOW + f'Стек: {stack}' + RESET)




# Основной (верхний цикл).
# Перебираем все вершины до тех пор, пока остаются непосещенные
for v in vertices:
    while True in new:
        dfs(v)


print(f'Списки смежности:\t {adj_list}')
print(f'Древесные  ребра:\t {wood_edges}')
print(f'Обратные   ребра:\t {back_edges}')
print(f'Прямые     ребра:\t {forward_edges}')
print(f'Поперечные ребра:\t {cross_edges}')
print(f'Err(mustbeempty):\t {errors_edges}')
print(f'Нумерация вершин:\t {d_numbers}')