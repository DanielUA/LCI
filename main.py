contacts = {}

def input_error(func):
    def wrapper(command):
        try:
            return func(command)
        except (TypeError) as e:
            return f"Input error of type: {e}"
        except (IndexError) as e:
            return f"Input error: {e}"
        except (ValueError) as e:
            return f"Input 3 arguments only(example: coammand name phone): {e}"
        except (KeyError) as e:
            return f"Input error: {e}"
        except Exception as e:
            return f"Command error"
    return wrapper

@input_error
def add(command):
    com, name, phone = command.split()
    if not com == "add":
        raise Exception("Incorect command name, try again")
    if name in contacts:
        raise KeyError("This name is exist")
    
    contacts[name] = phone
    
@input_error
def change(command):
    com, name, phone = command.split()
    if not com == "change":
        raise Exception("Incorect command name, try again")
    if not name in contacts:
        raise KeyError("This name is not exist")
    
    contacts[name] = phone

@input_error
def phone(command):
    com, name = command.split()
    if not com == "phone":
        raise Exception("Incorect command name, try again")
    if not name in contacts:
        raise KeyError("This name is not exist")
    
    return f"{name} has phone {contacts[name]}"

@input_error
def show_all(command):
    if command != "show all":
        raise Exception("Incorect command name, try again")
    result = [f"{k}-{v}" for k,v in contacts.items()]        
    
    return "\n".join(result)


COMMANDS = {   
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    }

@input_error
def command_action(command):
    for el in COMMANDS:
        if command.startswith(el):
            return COMMANDS[el]
    raise Exception("Incorect command name, try again")


def main():
    while True:
        command = input("Enter your command: ").lower()
        if command in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can i help you?")
            continue
        func = command_action(command)
        if func == "Command error":         
            print(func)
            continue
        result = func(command)
        if result == "break":
            break
        elif result:
            print(result)


if __name__ == "__main__":
    main()