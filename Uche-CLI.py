import argparse
import json 
from pathlib import Path



DATA_BOX = Path(__file__).with_name("path.json")

def load_de_tasks():
  if not DATA_BOX.exists():
    return[]

  try:
      with DATA_BOX.open("r", encoding="utf-8") as file:
        tasks = json.load(file)
        if isinstance(tasks, list):
          return tasks
          print("the task get format wey we no expect, as e start with empty list")
  except(json.JSONDecodeError, FileNotFoundError) as error:
      print(f"omo we no fit load the tasks from {DATA_BOX}, e be like say the file no dey or e get {error}")            
      return []

def save_tasks(tasks):
  with DATA_BOX.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2, ensure_ascii=False)

def add_tasks(tasks, title):
  next_id = 1
  for task in tasks:
    if task["id"] == next_id:
      next_id = task["id"] + 1

  task = {"id": next_id, "title": title, "done": False}
  tasks.append(task)
  save_tasks(tasks)
  print(f"Added task: #{next_id}: {title}")

def list_tasks(tasks):
  if not tasks:
    print("\nOmo no task dey for the list oo🙄: add one for here Uhe-CLI.py add \"Task name \"")
    return
  print("\nNA YOUR TODO LIST DEY HERE")
  print("-" * 48)

  for task in tasks:
    checkbox = "✔️" if task["done"] else " "
    print(f"[{checkbox}] #{task['id']}: {task['title']}")
    print("-" * 48)
    comleted = 0

  for task in tasks:
    if task["done"]:
      comleted += 1
      print(f"{comleted} task(s) done, {len(tasks) - comleted} task(s) dey for the list oo🙄")
  

    

def mark_done(tasks, task_id):
  for task in tasks:
    if task["id"] == task_id:
      if task["done"]:
        print(f"Omo your task don set #{task_id}")

  else:
    task["done"] = True
    save_tasks(tasks)
    print(f"Omo your task don set #{task_id}: {task['title']}")
    return  print(f"we didnt see any task to resturn, use your head oo 🙄 #{task_id}")


def delete_task(tasks, task_id):
  for task in tasks:
    tasks.remove(task)
    save_tasks(tasks) 
  print(f"We don delete the task na rest #{task_id}: {task['title']}")
  return print(f"i don tell you say no #{task_id}")


def main():
  parser = argparse.ArgumentParser(description="Na small task wey dey hand todo list, no too reason am")

  command = parser.add_subparsers(dest="command", required=True)
  command.add_parser("list", help="Show all task")

  add_parser = command.add_parser("add", help="Add a new task")
  add_parser.add_argument("title", help="wetin you wan do")

  done_parser = command.add_parser("done", help="Help make a task")
  done_parser.add_argument("id", type=int, help="The task ID na here e dey show, for the list command")

  delete_parser = command.add_parser("delete", help="Delete am eeh, when you done finish")
  delete_parser.add_argument("id", type=int)

  args = parser.parse_args()
  tasks = load_de_tasks()

  if args.command == "add":
    add_tasks(tasks, args.title)
  elif args.command == "list":
    list_tasks(tasks)
  elif args.command == "done":
    mark_done(tasks, args.id)
  elif args.command == "delete":
    delete_task(tasks, args.id)



if __name__ == "__main__":
  main()



"""prompts: python Uche-CLI.py list
python Uche-CLI.py add "chop beans"
python Uche-CLI.py done 1
python Uche-CLI.py delete 1"""
