import timeit
import matplotlib.pyplot as plt

def find_coins_greedy(coins: list, amount: int) -> dict:
    """
    Жадібний алгоритм для видачі решти.
    Він завжди вибирає найбільший доступний номінал.
    """
    result = {}
    # Сортуємо монети від найбільшого до найменшого, щоб брати найбільші першими

    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            # Визначаємо, скільки монет цього номіналу поміщається в суму
            count = amount // coin
            if count > 0:
                result[coin] = count
                # Віднімаємо вартість цих монет від загальної суми
                amount = amount - (coin * count)
    return result

def find_min_coins(coins: list, amount: int) -> dict:
    """
    Алгоритм динамічного для видачі решти.
    Гарантує найоптимальніше рішення для будь-якого набору номіналів.
    """

    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    # used_coins[i] буде зберігати номінал останньої монети, доданої для досягнення суми
    used_coins = [0] * (amount + 1)

    # Проходимо по всіх сумах від 1 до amount
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                # Якщо поточна монета дозволяє отримати меншу кількість монет для суми s
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    used_coins[s] = coin

    # Якщо для заданої суми рішення не знайдено ( неможливо скласти суму)
    if min_coins[amount] == float('inf'):
        return {}
    
    # Відновлюємо результат, рухаючись назад від amount до 0
    result = {}
    current_sum = amount
    while current_sum > 0:
        coin = used_coins[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin

    return result


def compare_algorithms():
    coins_list = [50, 25, 10, 5, 2, 1]
    
    # Значення для тестування (більше 2500 динамічний алгоритм стає дуже повільним)
    test_amounts = range(10, 1000, 100) 
    
    greedy_times = []
    dp_times = []

    print(f"{'Amount':<10} | {'Greedy Time (s)':<20} | {'DP Time (s)':<20}")
    print("-" * 60)

    for amount in test_amounts:
        # тестуємо Жадібний алгоритм
        # запускаємо його 10 разів і беремо середній час виконання: number=10 
        t_greedy = timeit.timeit(lambda: find_coins_greedy(coins_list, amount), number=10)
        
        # Тестуємо Динамічний аллгоритм так само:
        t_dp = timeit.timeit(lambda: find_min_coins(coins_list, amount), number=10)
        
        greedy_times.append(t_greedy)
        dp_times.append(t_dp)
        
        print(f"{amount:<10} | {t_greedy:.6f}             | {t_dp:.6f}")

    # Графіки
    plt.figure(figsize=(10, 6))
    plt.plot(test_amounts, greedy_times, label='Жадібний Алгоритм', color='green', marker='o')
    plt.plot(test_amounts, dp_times, label='Алгоритм Динамічного програмування', color='red', linestyle='--')
    
    plt.title('Тест швидкості: Жадібний vs Динамічне програмування')
    plt.xlabel('Target Amount (Sum)')
    plt.ylabel(f'Час виконання ,секунди (середня з 10 виконаннь)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    compare_algorithms()
