from threading import Thread

threads = []


def work():
    print('work')


def study():
    print('study')


def rest():
    print('rest')


def sleep():
    print('sleep')

threads.append(Thread(target=work))
threads.append(Thread(target=study))
threads.append(Thread(target=rest))
threads.append(Thread(target=sleep))

for th in threads:
    sleep()