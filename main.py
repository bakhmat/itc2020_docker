import sys
from time import sleep

if __name__ == "__main__":
    print(sys.argv[1])
    num = int(sys.argv[1])
    for i in range(num):
        print (str(i)+" "+str(i*i*i))
        sleep(1)
