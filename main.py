from subprocess import run
from pyautogui import press, typewrite
from time import sleep


def main():
    run(['start'], shell=True)
    sleep(0.1)

    # ユーザー名・パスワード・データベース名を変更↓
    typewrite("mysql -u root -proot dwh")

    press("enter")


if __name__ == '__main__':
    main()
