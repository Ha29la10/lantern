import argparse
import stoarge
def main():
    parser = argparse.ArgumentParser(description="Lantern CLI")
    sub = parser.add_subparsers(dest="command", required=True)

# The add command
    add_parser = sub.add_parser("add")
    
    # The list command defined on a single line
    list_parser = sub.add_parser("list")
    list_parser.add_argument(
    "--sort",
    action="store_true",
    help="Sort tasks by title"
)

    args = parser.parse_args()

    if args.command == "add":
        print("Executing the add command...")
    elif args.command == "list":
        tasks = stoarge.load()

        if not tasks:
            print("No tasks found.")
            return

        if args.sort:
            tasks = sorted(tasks, key=lambda task: task["title"].lower())

        for task in tasks:
            status = "Done" if task["done"] else "Pending"
            print(f"{task['title']} - {status}")
    elif args.command == "Omar":
        print("Executing the Omar command...")

if __name__ == "__main__":
    main()