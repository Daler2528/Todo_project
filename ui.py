session_user = None
from serviceses import AuthService , TodoService
from models import User
from exceptions import BedRequestException


def main_menu():
    if session_user:
        print("1 My Todo")
        print("2 Create Todos")
        print("3 Update Todo")
        print("4 delete Todo")
    else:
        print("1 login")
        print("2 Register")

    ch = input("Enter ->>")
    if session_user:
        user_manu(ch)
    else:
        auth_menu(ch)

def auth_menu(ch):
    global session_user
    auth_servise = AuthService()
    try:
        match ch:
            case "1":
                username = input("Username:")
                password = input("Password:")
                session_user = auth_servise.login_user(username=username,password=password)
            case "2":
                username = input("Username:")
                password=input("Password:")
                email=input("Email:")
                phone=input("Phone:")
                auth_servise.register_user(User(username=username,password=password,email=email,phone=phone))
                print("User successfully registred")
    except BedRequestException as e:
        print(e)
    main_menu()

def user_manu(ch):
    global session_user
    user_todo = TodoService(user=session_user)
    match ch:
        case "1":
            data = user_todo.my_todos()

            for todo in data:
                print(" | ".join(list(map(str, todo))))
        case "2":
           title = input("Enter Todo Title:")
           user_todo.create_todo(title=title)
        case "3":
            todo_id = input("Enter Todo id:")
            print("Choose Status:")
            print("1 todo:")
            print("2 process:")
            print("3 done:")
            s = input("Choose Status:")
            match s:
                case "1":
                    status = "todo"
                case "2":
                    status = "process"
                case "3":
                    status = "done"
                    user_todo.update_todo(todo_id=todo_id , status=status)
        case "4":
             todo_id = input("Enter Todo id:")
             user_todo.delete_todo(todo_id=todo_id)
    main_menu()





if __name__ == '__main__':
    main_menu()















