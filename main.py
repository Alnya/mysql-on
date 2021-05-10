from subprocess import run
from pyautogui import press, typewrite
from time import sleep
from settings import get_user, get_password, get_database


def main():
    user = get_user()
    password = get_password()
    database = get_database()

    command = f"mysql -u {user} -p{password} {database}"

    run(['start'], shell=True)
    sleep(0.1)

    typewrite(command)
    press("enter")


if __name__ == '__main__':
    main()
