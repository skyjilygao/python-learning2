import _thread
import time


def start(thread_name, count):
    for i in range(10):
        time.sleep(count)
        localtime = time.localtime(time.time())
        print(thread_name, i, '时间：', time.strftime('%y-%m-%d %H:%M:%S', localtime))


if __name__ == '__main__':
    _thread.start_new_thread(start,('thread_1',3))
    _thread.start_new_thread(start,('thread_2',2))
    _thread.start_new_thread(start,('thread_3',1))
    while 1:
        pass

