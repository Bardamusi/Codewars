"""
1 kyu - Faberge easter eggs crush test [linear]
This is the SUPER performance version of Faberge Easter Eggs

You task is exactly the same as that kata. But this time, you should output result % 998244353,
or otherwise the result would be too large.
"""
MOD = 998244353


def height(n, m):
    h, t = 0, 1
    for i in range(1, n + 1):
        t = t * (m - i + 1) // i
        h += t % MOD
    return h % MOD

if __name__ == "__main__":
    print("should work for some advanced tests")
    print(height(13, 550), 621773656)
    print(height(531, 550), 424414512)
    print('<COMPLETEDIN::>')
    print("should work for some serious tests :)")
    print(height(10 ** 4, 10 ** 5), 132362171)
    print(height(8 * 10 ** 4, 10 ** 5), 805097588)
    print(height(3000, 2 ** 200), 141903106)
    print(height(8 * 10 ** 4, 4 * 10 ** 4), 616494770)
    print(height(4 * 10 ** 4, 8 * 10 ** 4), 303227698)
    print('<COMPLETEDIN::>')