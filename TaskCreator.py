# Functions
def addTask(taskList):
    taskList.append(input("Enter task: "))
    return taskList


def removeTask(taskList):
    try:
        taskList.pop(int(input("Enter task number to remove: "))-1)
    except (ValueError, IndexError):
        print("Invalid task number.")
    return taskList


def markComplete(taskList, tasksCompleted):
    try:
        completedTask = int(input("Enter task number to mark complete: "))-1
        wordCrossed = ''.join([c + '\u0336' for c in taskList[completedTask]])
        tasksCompleted.append(wordCrossed)
        taskList.pop(completedTask)
    except (ValueError, IndexError):
        print("Invalid task number.")
    return taskList, tasksCompleted


def display_tasks(tasks, tasksCompleted, titleCharCnt):
    print("------------------------ Task List -------------------------")
    if not tasks:
        print("-                                                          -")
    for i, task in enumerate(tasks):
        print(f"- {i+1}. {task}{' ' * (titleCharCnt-6-len(task))}-")
    print("------------------------------------------------------------\n")
    print("------------------------ Completed -------------------------")
    if not tasksCompleted:
        print("-                                                          -")
    for task in tasksCompleted:
        task_length = len(task) // 2  # Each character is followed by a strikethrough character
        print(f"- {task}{' ' * (titleCharCnt-3-task_length)}-")
    print("------------------------------------------------------------\n")


def display_menu():
    print("------------------------ CipherTask ------------------------")
    print("- 1. Add                                                   -")
    print("- 2. Remove                                                -")
    print("- 3. Mark Complete                                         -")
    print("- 4. Quit                                                  -")
    print("------------------------------------------------------------\n")


def main():
    tasks = []
    tasksCompleted = []
    title = "------------------------ CipherTask ------------------------"
    titleCharCnt = len(title)

    programRun = True
    while programRun:
        display_menu()
        display_tasks(tasks, tasksCompleted, titleCharCnt)

        choice = input("Pick an option: ")
        if choice == "1":
            tasks = addTask(tasks)
        elif choice == "2":
            tasks = removeTask(tasks)
        elif choice == "3":
            tasks, tasksCompleted = markComplete(tasks, tasksCompleted)
        elif choice == "4":
            programRun = False
        else:
            print("Invalid choice. Please select a valid option.")
        print("\n")


if __name__ == "__main__":
    main()
