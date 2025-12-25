print("Select Mode:")
print("1. Custom Detection Mode")
print("2. Assistive Mode")

choice = input("Enter choice: ")

if choice == "1":
    from src.modes.custom_mode import *
elif choice == "2":
    from src.modes.assistive_mode import *
else:
    print("Invalid choice")
