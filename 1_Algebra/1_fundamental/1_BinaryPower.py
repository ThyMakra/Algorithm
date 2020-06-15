## Recursive: a^n
def binpowre(a, n):
    if n == 0: return 1
    res = binpowre(a, int(n / 2))
    if n % 2: # odd
        return res * res * a # (a ^ (2x + 1))
    else:
        return res * res

## Loop : a^n
def binpow(a, n):
    res = 1
    while n > 0:
        if n & 1: # AND with binary number = 1; return 0 if even, 1 if odd
            res = res * a
        a = a * a
        n >>= 1 # binary right-shift by 1 bit
    return res
    
""" Test """
x = binpow(2, 12)
print(x)

## Modulo arithmetic: a ^ b (mod n)
def binpowmod(a, b, n):
    a %= n
    res = 1
    while b > 0:
        if b & 1: # AND with binary number = 1; return 0 if even, 1 if odd
            res = res * a % n
        a = a * a % n
        b >>= 1 # binary right-shift by 1 bit
    return res
""" Test power mod """
print(binpowmod(2, 4, 3))