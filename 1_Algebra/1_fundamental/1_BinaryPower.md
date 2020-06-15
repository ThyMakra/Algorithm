## Overview
- Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to calculate a^n using only O(log n) multiplications (instead of O(n) multiplications required by the naive approach).
- A trick to calculate the result of a number raising to a large input.

- Reference: https://cp-algorithms.com/algebra/module-inverse.html

### Use
- It also has important applications in many tasks unrelated to arithmetic, since it can be used with any operations that have the property of _associativity_:
    (X⋅Y)⋅Z = X⋅(Y⋅Z)

- It applies to modular multiplication, to multiplication of matrices and to other problems.

## Algorithm
- The idea of binary exponentiation is, that we split the work using the binary representation of the exponent. Example: 

    3<sup>13</sup> = 3<sup>1101<sub>2</sub></sup> = 3<sup>1</sup>⋅3<sup>4</sup>⋅3<sup>8</sup>

## Application
### 1. Large exponents modulo a number
- Problem: Compute x<sup>n</sup> mod m. \
For instance it is used in computing the modular [multiplicative inverse](https://cp-algorithms.com/algebra/module-inverse.html).

- Solution: Since the modulo operator does not interfere with multiplications, we just replace multiplication with modulo multiplication.
    - __Note__: If m is a prime number we can speed up a bit this algorithm by calculating x<sup>n mod (m−1)</sup> instead of x<sup>n</sup>. \
    This follows directly from [Fermat's little theorem](https://cp-algorithms.com/algebra/module-inverse.html#toc-tgt-2).

### 2. Effective Computation of Fibonancci numbers
