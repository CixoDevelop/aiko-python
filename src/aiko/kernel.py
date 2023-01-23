from .process import process_types_t, process_t
from .message_box import message_box_t

class kernel_t:


    def __init__(self):
        self.__processes = []
        self.__last_changed = {}


    def create_process(self, new_process):
        self.__processes[new_process.get_pid()] = new_process


    def kill_process(self, process_pid):
        if self.kernel_check_pid_empty(process_pid):
            return False

        del(self.__processes[process_pid])

        return True

    
    def check_pid_empty(self, process_pid):
        return not process_pid in self.__processes


    def scheduler(self):
        while True:
            for process in self.__last_changed:
                process.worker(self, process)

                if not process.message_box.is_readable():
                    self.__last_changed.remove(process)

            for process in self.__processes:
                if process.get_type() == process_types_t.CONTINUOUS:
                    process.worker(self, process)
                    continue

                if process.message_box.is_readable():
                    process.worker(self, process)


    def trigger_signal(self, signal):
        for process in self.__processes:
            if process.get_type() == process_types_t.SIGNAL:
                process.message_box.send(signal)
                self.__last_changed.add(process)


    def remove(self):
        self.__processes = []
        self.__last_changed = {}


    def process_message_box_send(self, process_pid, message):
        process = self.__processes[process_id]

        process.message_box.send(message)
        self.__last_changed.add(process)
