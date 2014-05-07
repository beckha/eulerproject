# -*- coding:utf-8 -*-

if __name__ == '__main__':
   res = 0
   for i in range(100,1000):
     for j in range(100,1000):
        temp = str(i*j)
        if temp == temp[::-1] and i*j > res:
           res = i * j
   print res
