#!/usr/bin/python3 
'''it is called shebang in python3 why we use in to say interpreter that i want to ran from python3 not python2'''
#array.py
from array import *
def p(): 
    #creating array in python only suports 1 dimenstional   
    vals =array('I',[5,6,7,8,9])
    print(vals[0: ])
    for i in range(0,5):
        print(vals[i])
    for e in vals:
        print(e)
    #coping other array
    newarry =array(vals.typecode,(a for a in vals))
    print(newarry[0:])
def ip():
    #taking user input from arrays
    v = array('I',[])
    n = eval(input('please enter the size of array : '))
    for e in range(n):
        i = eval(input(f'enter the value of {e+1} :'))
        v.append(i)
    print(v[0:])
    # searching a element in array 
    e = eval(input('please enter a value to search in array : '))
    o=0
    for o in v:
        if o==e:
            print('element found',e,sep=' ')
            break
    else:
        print('no value found in this array')
def main():
    p()
    ip()
main()
