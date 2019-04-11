import schedule
import time


def start():
    print('hello')


if __name__ == '__main__':
    start()
    schedule.every(2).minutes.do(start)

    while True:
        schedule.run_pending()
        time.sleep(1)
