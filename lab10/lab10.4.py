
def knapsack(weights, values, max_weight):
    n = len(weights)
    # Создаем матрицу для хранения максимальной стоимости, которую можно унести в рюкзаке
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Заполняем матрицу
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            # Если текущий предмет может поместиться в рюкзак
            if weights[i - 1] <= w:
                # Выбираем максимальную стоимость из двух вариантов:
                # 1. Не включать текущий предмет в рюкзак
                # 2. Включить текущий предмет в рюкзак
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Текущий предмет не может поместиться в рюкзак, поэтому не включаем его
                dp[i][w] = dp[i - 1][w]

    # Возвращаем максимальное значение, которую можно унести в рюкзаке
    return dp[n][max_weight]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 7
print(knapsack(weights, values, max_weight))  # 9
