import threading
import ctypes as cp
import multiprocessing as mp


class ThreadTool(object):

    def __init__(self) -> None:
        self.terminate = False

    def Terminate(self):
        self.terminate = True

    def Run(self, _cycle: bool, _function, *_args):
        if _cycle:

            def cycle():
                while self.terminate == False:
                    _function(*_args)

            threading.Thread(target=cycle).start()
        else:
            threading.Thread(target=_function, args=(_args)).start()


# ---------------------------------------------------------------------------- #
class ProcessCycleHelper(object):

    def __init__(self, _terminateTag, _function, _args) -> None:
        while _terminateTag.value == False:
            _function(*_args)


class ProcessTool(object):

    def __init__(self) -> None:
        self.terminate = mp.Value(cp.c_bool, False)

    def Terminate(self):
        self.terminate.value = True
        self.Task.terminate()
        self.Task.join()

    def Run(self, _cycle: bool, _function, *_args):
        if _cycle:
            self.Task = mp.Process(target=ProcessCycleHelper,
                                   args=(self.terminate, _function, _args))
            self.Task.start()
        else:
            self.Task = mp.Process(target=_function, args=(_args))
            self.Task.start()
