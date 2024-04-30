class Student:
   
   # s_no = 1
   # name = "Mona"
   # age = 18
   # city = "Jaipur"
   
   def __init__(self, id, name, age, city):  # here self is keyword(object) of class Stuent, it takes referene from class Student
      self.Student_id = id  # Student_id is identifier it can be any variable
      self.Student_name = name
      self.Student_age = age
      self.Student_city = city
      
      pass
   
   def output(self):
      print(self.Student_id,self.Student_name, self.Student_age, self.Student_city)
      
obj1 = Student(1,"Mona",99,"Jaipur")
obj1.output()

obj2 = Student(2,"Pooja",44,"Darbhanga")
obj2.output()

obj3 = Student(3,"Yash",10,"Laheriasarai")
obj3.output()