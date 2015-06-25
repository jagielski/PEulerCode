I currently plan to implement some solutions of late problems (p516, p233, maybe others that spark my interest), then work on finishing the first 100 problems.

This is just a dump of all the code I have written for Project Euler problems.
My general strategy for them is to think about them mathematically first, hopefully coming up with some strategies for optimization.
If necessary, I will make some test functions so I can conjecture a mathematical rule. After this comes the code, which is generally not too tricky-
it just requires one to keep their mind on efficiency and readability, so that the code terminates in a reasonable amount of time and is modifiable
just in case changes need to be made.

I have also written some overarching functions in numthy.py and eratosthenes.py, which contain some number theoretic algorithms which are useful in
several situations. eratosthenes.py is code I obtained online (although it is not difficult to implement) for the sieve of eratosthenes, which I have
used to generate files of all primes below several powers of 10.

Some problems I enjoyed solving:
p243.py
p346.py, which was easy to solve upon realizing every number n is a repunit in base n-1
p347.py
p381.py, my personal favorite, but that is just because I really like Wilson's theorem
p516.py, it was fun using some simple number theory to work towards an efficient solution


Some basic problems:
p301.py, which was really really easy once I learned how Nim is won
p206.py, which was brute force plus some simple observations
p99.py, just uses logarithms to make calculations smaller

Incomplete solutions - I enjoy coming back to these and approaching them in different ways:
p508.py, I am going to try to find some elegant resolution for this one - the math is messy as of now
p504.py, an interesting problem - I believe I just need to read up on some theorems for this one
p357.py, my first thought was just to enumerate squarefree integers, but, as I feared, it is not so simple
p288.py, I haven't really put thought into this one, just wrote some preliminary code
p282.py, I wrote this one a long time ago and haven't come back to it

Recently solved:
p407.py - got this working, although it took a long time to run. people on the boards were using C/C++ and getting much faster times
p516.py - got this working - removed 2,3,5 from the hamming primes list, as that resulted in doublecounting many values
p051.py - simple bruteforce using a presieved set of primes
