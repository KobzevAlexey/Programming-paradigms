sum_list([], 0). % Базовый случай: сумма пустого списка равна 0

sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum), % Рекурсивно вычисляем сумму оставшегося списка
    Sum is Head + TailSum. % Вычисляем общую сумму как сумма головы списка и суммы остатка