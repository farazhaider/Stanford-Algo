#!/usr/bin/python
import random

def merge(left, right):
   i,j = 0,0
   result=[]
   while i<len(left) and j<len(right):
     if left[i] <= right[j]:
        result.append(left[i])
        i += 1
     else:
        result.append(right[j])
        j += 1

   result += left[i:]
   result += right[j:]
   return result


def mergesort(list):
   if len(list) < 2:
       return list
   middle = len(list) / 2
   left = mergesort(list[:middle])
   right = mergesort(list[middle:])
   return merge(left, right)


a=range(999999)
random.shuffle(a)
print mergesort(a)
print "finished sorting", len(a), " numbers"
