from threading import Thread
from bot import run_bot
from game import run_game

if __name__ == '__main__':
    threads = [
        Thread(target=run_bot),
        Thread(target=run_game)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
