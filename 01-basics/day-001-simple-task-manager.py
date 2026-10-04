# simple task manager

import os
# global variable
tasks = []

# class task
class task :
    def __init__(self, title, description, priority,due_time, status="pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_time = due_time
        self.status = status

    
    def mark_as_complete(self):
        self.status = "complete"
        

    def mark_as_inprogress(self):
        self.status = "inprogress"
        

    def modify_title(self, new_title):
        self.title = new_title
        



# help function
def is_empty() :
    if not tasks :
        print('not tasks to action add first!')
        return True


def clear() :
    os.system('cls')
    



# main actions
def create_task() :
    title = input("Enter title of task: ")
    description = input("Description: ")
    priority = input("priority:[L,M,H]: ")
    due_time = input("due time: ex [02-10-2026]: " )
    
    return task(title, description, priority, due_time)


def delete_task(task_id):
        tasks.pop(task_id)
        


def show_all_tasks():
    if not tasks :
        print("not tasks yet!")
    else :
        j = 1
        for i in tasks:
            
            if i.status == "pending" :
                print(f'{j}. [ ] {i.title}')
            elif i.status == "inprogress" :
                print(f'{j}. [>] {i.title}')
            elif i.status == "complete" :
                print(f'{j}. [x] {i.title}')
            j+=1



def ui_app() :
    print('-'*30)
    print('1. add new task')
    print('2. mark task as complete')
    print('3. mark task in progress')
    print('4. delete task')
    print('5. modify task title')
    print('0. exit')
    print('-'*30)
    



# heart of app
def main() :
    while True :
        show_all_tasks()
        ui_app()
        choose = int(input('choose action : '))
        
        
        if choose == 1 :
            tasks.append(create_task())
            clear()
            
            
        elif choose == 2 :
            if is_empty() :
                continue
            task_id = int(input('enter number of task: '))
            if task_id > len(tasks) or task_id < 1 :
                print('invalid id')
                continue
            else :
                tasks[task_id-1].mark_as_complete()
            clear()    
        
        
        elif choose == 3 :
            if is_empty() :
                continue
            task_id = int(input('enter number of task: '))
            if task_id > len(tasks) or task_id < 1 :
                print('invalid id')
                continue
            else :
                tasks[task_id-1].mark_as_inprogress()
            clear()


        elif choose == 4 :
            if is_empty() :
                continue
            task_id = int(input('enter number of task: '))
            if task_id > len(tasks) or task_id < 1 :
                print('invalid id')
                continue
            else :
                delete_task(task_id -1)
            clear()
        
        
        elif choose == 5 :
            if is_empty() :
                continue
            task_id = int(input('enter number of task: '))
            if task_id > len(tasks) or task_id < 1 :
                print('invalid id')
                continue
            else :
                new_title = input('enter new title: ')
                tasks[task_id-1].modify_title(new_title)
            clear()
            
            
        elif choose == 0 :
            print('bye!')
            return 0
        
        
        else :
            print('invalid choose! ')
            clear()
            continue
            



# end point 
main()
