# Functions
def addTask(taskList):
    taskList.append(input("Enter task: "))
    return taskList


def removeTask(taskList):
    taskList.pop(int(input("Enter task number to remove: "))-1)
    return taskList


def markComplete(taskList, tasksCompleted):
    completedTask = int(input("Enter task number to mark complete: "))-1
    wordCrossed = ''
    for c in taskList[completedTask]:
        wordCrossed = wordCrossed + c + '\u0336'

    tasksCompleted.append(wordCrossed)
    taskList.pop(completedTask)

    return taskList, tasksCompleted


# variables
tasks = []
tasksCompleted = []
title = "------------------------ CipherTask ------------------------"
titleCharCnt = len(title)

# menu selection
programRun = True
while programRun:
    print("------------------------ CipherTask ------------------------")
    print("- 1. Add                                                   -")
    print("- 2. Remove                                                -")
    print("- 3. Mark Complete                                         -")
    print("- 4. Quit                                                  -")
    print("------------------------------------------------------------\n")
    print("------------------------ Task List -------------------------")
    if tasks == []:
        print("-                                                          -")
    for i in range(len(tasks)):
        print("- "+str(i+1) + ". " + tasks[i], end="")
        print(" "*(titleCharCnt-4-len(tasks[i])) + "-")
    print("------------------------------------------------------------\n")
    print("------------------------ Completed -------------------------")
    if tasksCompleted == []:
        print("-                                                          -")
    for i in range(len(tasksCompleted)):
        print("- "+tasksCompleted[i], end="")
        print(" "*(titleCharCnt+1-len(tasksCompleted[i])) + "-")
    print("------------------------------------------------------------\n")

    choice = input("Pick an option: ")
    if choice == "1":
        tasks = addTask(tasks)
    elif choice == "2":
        tasks = removeTask(tasks)
    elif choice == "3":
        tasks, tasksCompleted = markComplete(tasks, tasksCompleted)
    elif choice == "4":
        programRun = False
    print("\n")
