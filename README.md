# AirBnB Clone - The Console

## Project Description
This project is the first step towards building a full-stack AirBnB clone web application. In this phase, we develop a command-line interface (command interpreter) to manage application data. This tool allows us to create, update, destroy, and manage data models (like Users, Places, States, Cities, etc.) without a graphical interface.

---

## Command Interpreter

### How to Start It
To start the command interpreter in interactive mode, run the console file from your terminal:
```bash
./console.py
```

To run a command in non-interactive mode (passing commands via pipe), use:
```bash
echo "help" | ./console.py
```

### How to Use It
Once inside the interpreter, you can use the following commands to manage your objects:
* `help` - Displays a list of available commands or documentation for a specific command.
* `quit` or `EOF` - Exits the command interpreter.
* `create <Class>` - Creates a new instance of a class, saves it to a JSON file, and prints its ID.
* `show <Class> <id>` - Prints the string representation of an instance based on the class name and ID.
* `destroy <Class> <id>` - Deletes an instance based on the class name and ID.
* `all` or `all <Class>` - Prints all string representations of all instances, or all instances of a specific class.
* `update <Class> <id> <attribute name> "<attribute value>"` - Updates an instance based on the class name and ID by adding or updating an attribute.

### Examples

**Interactive Mode:**
```bash
\$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
(hbnb) show User 0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d
[User] (0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d) {'id': '0a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d', 'created_at': datetime.datetime(...)}
(hbnb) quit
\$
```

**Non-Interactive Mode:**
```bash
\$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
\$
```

