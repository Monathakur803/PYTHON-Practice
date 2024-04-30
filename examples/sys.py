import sys

if len(sys.argv)>2:
    print("Too few arguments")
elif len(sys.argv) > 2 :
    print("too many argument")
else:
    print("hello, my name is ", sys.argv[0])