# OOP Basics not prosedural programming

class Book:
    title = ""
    author = ""
    pages = 0
    

my_book = Book()

my_book.title = "Origin"
my_book.author = "Dan Browm"
my_book.pages = 542

print(my_book.title)

second_book = Book()

second_book.title = "Cpp"
second_book.author = "Me"
second_book.pages = 544


# ---

class Screen :
    name = ""
    model = ""
    resulution_per_pixel = 0
    size = 0
    
    def print(self):
        print('name: ',self.name)
        print('model: ',self.model)
        print('resulution: ',self.resulution_per_pixel)
        print('size: ',self.size)
        print('-'*50)



MSI = Screen()

MSI.name = "MSI"
MSI.model = "sw32fg"
MSI.resulution_per_pixel = 500
MSI.size = 32

# method
MSI.print()



# ---

# magic method

class Player :
        
    
    def __init__(self, name, height, team): # initialize
        self.name = name
        self.height = height
        self.team = team
        
    def print(self):
            print('name: ',self.name)
            print('height: ',self.height)
            print('team: ',self.team)
            print('-'*50)

player1 = Player("Messi", 173, "Barcalona") 

player1.print() # Player.print(player1) 


# ---

class Task :
    def __init__(self, title, description, due_time, status='incomplete'):
        self.title = title
        self.description = description
        self.due_time = due_time
        self.status = status


def create_task() :
    title = input('enter title of task : ')
    description = input('enter description : ')
    due_time = input('enter due_time : ')
    
    return Task(title, description, due_time)


Task1 = create_task() # Task1 = Task(title, description, due_time)

print(Task1.title)

# ---