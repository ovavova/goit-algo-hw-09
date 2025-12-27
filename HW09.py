

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

    # used_coins[i] буде зберігати номінал останньої монети, доданої для досягнення суми i
    # Це потрібно для відновлення результату (які саме монети ми взяли)
    used_coins = [0] * (amount + 1)

    # Проходимо по всіх сумах від 1 до amount
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                # Якщо поточна монета дозволяє отримати меншу кількість монет для суми s
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    used_coins[s] = coin

    # Якщо для заданої суми рішення не знайдено (наприклад, неможливо скласти суму)
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



def main():
    coins_list = [50, 25, 10, 5, 2, 1]

    target_amount = 113

    print(f"Сума для видачі: {target_amount}")

        # Тест жадібного алгоритму
    greedy_result = find_coins_greedy(coins_list, target_amount)
    print("Greedy Algorithm:", greedy_result)

        # Тест динамічного програмування
    dp_result = find_min_coins(coins_list, target_amount)
    print("Dynamic Programming:", dp_result)


if __name__ == "__main__":
    main()
