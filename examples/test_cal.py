from calc import square

def main():
   test_square()

def test_square():
   '''
   assert square(2) == 4
   assert square(3) == 9  # will give assertion error  so use try except concept of python
   '''
   try:
      assert square(2) == 4
   except AssertionError:
      print("2 square was not 4")
      
   try:
      assert square(3) == 9
   except AssertionError:
      print("3 square was not 9")
      
   try:
      assert square(-3) == 9
   except AssertionError:
      print("-3 square was not 9")
      
   try:
      assert square(-2) == 4
   except AssertionError:
      print("-2 square was not 4")
      
   try:
      assert square(0) == 0
   except AssertionError:
      print("0  square was not 0")
   '''
   if square(2) != 4:
      print("2 square was not 4")
   if square(3) != 9:
      print("3 square was not 9")
      
      '''
      
      
      
if __name__ == "__main__":
   main()
   