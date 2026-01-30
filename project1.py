from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
task_collection = db.tasks


def create_task(description):
    task = {'task': description}
    result = task_collection.insert_one(task)
    print(f"Task created with id: {result.inserted_id}")


def read_task():
    tasks = task_collection.find()
    for docs in tasks:
        print(docs['task'])


def count_tasks():
    print("Total tasks:", task_collection.count_documents({}))

    


while True:
    print("\n1. Create task")
    print("2. View tasks")
    print("3. Count tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter your task: ")
        create_task(description)

    elif choice == '2':
        read_task()

    elif choice == '3':
        count_tasks()

    elif choice == '4':
        break

    else:
        print("Provide a valid option")
