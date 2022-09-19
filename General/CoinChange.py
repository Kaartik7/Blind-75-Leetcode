def CoinChange(amount: int, coins: list) -> int:
    """
    Return the number of ways you can make up the amount using the given denomination of coins.
    You can assume that the amount of each coin is less than 5000.
    :param amount:
    :param coins:
    :return:
    """
    combinations = 0
    n = amount // min(coins)
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            for k in range(0, n + 1):
                if (coins[0] * i) + (coins[1] * j) + (coins[2] * k) == amount:
                    combinations += 1
    return combinations
