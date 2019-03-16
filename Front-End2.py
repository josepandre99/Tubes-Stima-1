import sys
import greedy

AA = sys.argv[1]
BB = sys.argv[2]


fin = open(AA, "r")
sk = fin.read()
sk = sk.split()

sktemp = [int(i) for i in sk]
sktemp.sort(reverse = True)

fin.close()

fout = open(BB, "w")
fout.write(greedy.hasil(sk))

fout.close()
