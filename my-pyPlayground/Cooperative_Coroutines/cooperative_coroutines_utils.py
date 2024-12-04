import subprocess
import time


def sleep(durationSec: int):

    timeToSleep = time.time() + durationSec
    while timeToSleep > time.time():
        yield


def run_shell_cmd(cmd: str):

    print("Run Command [ %s ]" % cmd)
    process = subprocess.Popen(
        cmd,
    )
