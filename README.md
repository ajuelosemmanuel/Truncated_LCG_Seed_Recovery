# Truncated LCG Seed Recovery

Python implementation of the attacks explained in the 2.7 part of [“Reconstructing
truncated integer variables satisfying linear congruences”](https://www.math.cmu.edu/~af1p/Texfiles/RECONTRUNC.pdf).

This part is explaining how we can attack a Truncated Linear Congruential Generator if we have either the Most Significant Bits or the Least Significant Bits.

Almost all the code is what me and my classmates did during [this project](https://github.com/ajuelosemmanuel/CRYPTA_Project), I only added code for the second case in this repo.

## How does this work ?

We have :

$X_{i+1} \leftarrow (aX_i + b) \pmod m$ and $Y_i \leftarrow \left \lceil{X_i/k}\right \rceil$ (or $\left \lfloor{X_i/k}\right \rfloor$, in the second case) where $b = 0$

Note : it is also possible to make an attack where $b \neq 0$, using the difference of two consecutive outputs of the PRNG.

For the second case, we use the fact that $m$ is odd. We can find it's inverse, and use it to get the Most Significant Bits - and thus we're solving the first case.

For a given $X_i$ and $n$ last bits given, we have :

$X_i = 2^n * Z_i + Y_i \pmod{m} $

with $Y_i$ being the last bits given and $Z_i$ the Most Significant Bits that we don't know yet.

Let $I$ be the inverse of $2^n \pmod{m}$ (it exists as $m$ is odd). We have :

$X_i*I = Z_i + Y_i*I \pmod{m}$

Thus, Z_i is lower than Y_i and therefore we are in the first case.

The first case is better explained in the article, but basically : we can make a matrix of the outputs and using Euclidean Lattices, we can attack the PRNG. This implementation uses LLL, and it's great wrapper in Python that is [fpylll](https://github.com/fplll/fpylll).

## Note

I couldn't test if my MSB code if running, as I added it from a machine that can't run it for the repo to be "complete". I'll gladly modify it in order to make it work if it has any problem.
