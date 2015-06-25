# phi(n^2)=nphi(n)
# then we only care about odds
# g(n)=sum(phi(2k+1))
primefile = open("primes108.txt")
primeli =[]
for line in primefile:
    primeli.append(int(line.strip()))
primeli=primeli[1:]