1. Get a remainder using bitwise operator with a number that is equal to `2^n - 1`:
- Since the binary number with the value of 2^n - 1 has all number 1, so we can use the & Operator to get the remainder of (n + 1).

        X % (2^n) == X % (2^n - 1)

For example: 589 = 1001001101<sub>2</sub>, 7 = 111<sub>2</sub>, 
so the result of 589 & 7 is the last 3 bits of 589. \
In other words, the list result from 1 to 589 will only range from 0 to 7 which is the same as when we do it with modulo 8.
