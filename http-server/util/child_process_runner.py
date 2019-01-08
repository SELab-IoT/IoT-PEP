import psutil
from time import sleep

### TODO:DEAD CODE. REMOVE LATER
class ChildProcessRunner(object):

    def __init__(self, parent_pid, command):
        """
        @type parent_pid: int
        @type command: string
        """
        self._child = None
        self._cmd = command
        self._parent = psutil.Process(pid = parent_pid)
        
    def run_child(self):
        """
        Start a child process by running self._cmd.
        Wait until the parent process (self._parent) has died, then kill the child.
        """
        print("Command : %s" % self._cmd)
        try:
            while self._parent.status == psutil.STATUS_RUNNING:
                sleep(1)
        except psutil.NoSuchProcess:
            pass
        finally:
            print("Terminate Child PID %s : " % self._child.pid)
            self._child.terminate()