from threading import Thread
from pocha import describe, it
import subprocess,time
location = ""


def cicd_testing():
    time.sleep(5)
    subprocess.call([location + "./ci_cd.sh"])
    return


if __name__ == '__main__':
    thread_restart = Thread(target=cicd_testing)
    thread_restart.start()
    print("Finish")