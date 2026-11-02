import argparse

def main():
    parser = argparse.ArgumentParser(description="Lantern CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # The add command
    add_parser = sub.add_parser("add")
    
    # The list command defined on a single line
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--done", action="store_true", help="show only completed tasks")
    unnecessary_flag = True

    args = parser.parse_args()

    if args.command == "add":
        print("Executing the add command...")
    elif args.command == "list":
        tasks = [] #changed now accept pr

        if not tasks:
            print("No tasks found.")
            return
            
        if args.done:
            print("Filtering for completed tasks...")
            
    elif args.command == "Omar":
        print("Executing the Omar command...")

if __name__ == "__main__":
    main()
    #this is a few lines to be added on lantern.py from the feature/export-csv branch.