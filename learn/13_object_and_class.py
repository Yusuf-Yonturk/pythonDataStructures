import matplotlib.pyplot as plt


# class Circle(object):
#   def __init__(self, radius, color):
#     self.radius=radius
#     self.color=color


# objecT=Circle(10,5)
# print(objecT)

class Car:
  __slots__=["make", "model", "color", "__speed"]
  max_speed=120 #Maximum speed in km/h

  #Constructor method (initalize instance attributes)
  def __init__(self, make: str, model: str,color: str,speed=0):
    self.make=make
    self.model=model
    self.color=color
    self.__speed=speed

  def accelerate(self,acceleration: int):
    if self.__speed + acceleration < Car.max_speed:
      self.__speed+=acceleration
    else:
      self.__speed=Car.max_speed

  #Method to get the current speed of the car
  @property
  def speed(self):
    return self.__speed
  
  @speed.setter
  def speed(self, new_speed: int):
    if 0 <=new_speed <=Car.max_speed:
      self.__speed=new_speed
    else:
      raise ValueError(f"Hız {new_speed} olamaz!  (0-{Car.max_speed})")

car1=Car("Toyota", "Supra", "Orange")
car2=Car("Ford", "Mustang", "Black")

print(car1.speed)
Car.speed=1
print(Car.speed)
print(car1.speed)

car1.accelerate(30)
car2.accelerate(20)

print(f"{car1.make} {car1.model} is currently at {car1.speed} km/h")
print(f"{car2.make} {car2.model} is currently at {car2.speed} km/h")

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r: float):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
    
RedCircle = Circle(10, 'red')
#RedCircle.drawCircle()
dir(RedCircle)
print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius=1
print(RedCircle.radius)
#RedCircle.drawCircle()

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
BlueCircle = Circle(radius=100)
print(BlueCircle.radius)
print(BlueCircle.color)
#BlueCircle.drawCircle()

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
BlueRectangle=Rectangle(2,3,'blue')
#BlueRectangle.drawRectangle()
print(BlueRectangle.height)
print(BlueRectangle.width)
print(BlueRectangle.color)

#Type your code here

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)
car1=Vehicle(200,20)
car2=Vehicle(180,25)
car1.assign_seating_capacity(5)
car2.assign_seating_capacity(4)
car1.display_properties()
car2.display_properties()

class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80


val = Graph(200)
print(val.id)

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    
    def __init__ (self, text):
        formattedText=text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText=formattedText.lower()
        self.fmText=formattedText
        
    def freqAll(self):        
        wordList=self.fmText.split()

        freqMap={}
        for word in set(wordList):
            freqMap[word]=wordList.count(word)
        return freqMap
        
        # Create dictionary
           
    def freqOf(self,word):
        freqDict=self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
    
t1=TextAnalyzer(givenstring)
print(t1.fmText)

print(t1.freqAll())

print(t1.freqOf("magna"))

