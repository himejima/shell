# -*- coding: utf-8 -*-
import sys
import random
import string

#print sys.argv

# sample
# @param パスワードの文字数
# $ python generate_password.py 2

# デフォルトは文字数を10文字にする
n = 10

if (len(sys.argv) > 2):
    print 'Usage:'
    print '$ python generate_password.py 2'
    exit()
elif (len(sys.argv) == 2):
    n = int(sys.argv[1])

#print n
#for i in range(n):
#    print i
#
#print [i for i in range(n)]
#
#print string.digits
#print string.ascii_letters
#
#print random.choice([2,3,9])
#
#
#print [random.choice(string.digits + string.ascii_letters) for i in range(10)]
#
#print ''.join(['1','2','3'])

print ''.join([random.choice(string.digits + string.ascii_letters) for i in range(n)])
