import argparse

def main():
    parser = argparse.ArgumentParser(description="Lantern CLI")
    sub = parser.add_subparsers(dest="command", required=True)

# The add command
    add_parser = sub.add_parser("add")
    
    # The list command defined on a single line
    list_parser = sub.add_parser("list")

    args = parser.parse_args()

    if args.command == "add":
        print("Executing the add command...")
    elif args.command == "list":
       tasks = []

    if not tasks:
        print("No tasks found.")
        return
    elif args.command == "Omar":
        print("Executing the Omar command...")

if __name__ == "__main__":
    main()