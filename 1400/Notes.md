# General

Counting odd number frequencies of characters because that is main property of a palindrome.

# python

- The soltution is 2d5fafca3fca4493c9900daef8d33a972952e6ca works fine. It is fairly fast. Anything else would be over optimization.
- Tried the memoization method in python. It is slower in this case. LOL.


# go

- The go solution works, but it is way slower for it.(ecec8d2604863ab8ad12b5ab1924f1620a41f080)
- It is clear I need to implement the memoization version. The hashing algo is the bottleneck.
- The memo method is the fastest for Go.