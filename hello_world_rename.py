import monkey
import sys
#-*- coding:utf-8 -*-
if __name__=="__main__":
    print('Hello monkeys')
    print('Starting to understand git')
    monkey.print_monkeys([0,1,2,3,4,5])

def print_palmtrees(num):
    for i in range(num):
        sys.stdout.write(' /|\\')
    sys.stdout.write('\n')
    for i in range(num):
        sys.stdout.write(' | ')
    sys.stdout.write('\n\n')


print_palmtrees(1)
Print("GITHUB")
