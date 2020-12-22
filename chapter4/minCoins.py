def recMC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList: list, change: int, minCoins: list) -> int:
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount

    return minCoins[change]


def dpMakeChange1(
    coinValueList: list, change: int, minCoins: list, coinsUsed: list
) -> int:
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


c1 = [1, 5, 10, 21, 25]
coinsUsed = [0] * 64
coinCount = [0] * 64
dpMakeChange1(c1, 63, coinCount, coinsUsed)

print("The changes for 63: ")
printCoins(coinsUsed, 63)
print("The changes for 52: ")
printCoins(coinsUsed, 52)
