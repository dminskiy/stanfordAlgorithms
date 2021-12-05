import time

def multiplyKaratsuba(val1, val2):
    if len(str(val1)) == 1 or len(str(val2)) == 1:
        return int(val1) * int(val2)
    else:
        m = max(len(str(val1)), len(str(val2)))
        m2 = m // 2

        a = int(val1) // 10 ** m2
        b = int(val1) % 10 ** m2
        c = int(val2) // 10 ** m2
        d = int(val2) % 10 ** m2

        z0 = multiplyKaratsuba(b, d)
        z1 = multiplyKaratsuba((a + b), (c + d))
        z2 = multiplyKaratsuba(a, c)

        return (z2 * 10 ** m) + ((z1 - z2 - z0) * 10 ** m2) + z0


if __name__ == '__main__':
    print('Let us multiply!')
    x = input("Enter value 1 : ")
    y = input("Enter value 2 : ")

    s = time.time()
    out_karatsuba = multiplyKaratsuba(x, y)
    kara_t = time.time() - s

    print(f'Karatsuba algorithm.\nResult: {out_karatsuba}\nExecution time: {round(kara_t, 5)}s')
