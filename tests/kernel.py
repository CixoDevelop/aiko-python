import unittest
import sys

sys.path.append("../src")
from aiko import process_t, process_types_t, kernel_t

class kernel_test(unittest.TestCase):

    def test_kernel_continuous(self):
        def simple_writer(kernel, process):
            process.parameter += 1
            print("Simple writer: " + str(process.parameter))

        def simple_ender(kernel, process):
            process.parameter -= 1

            if process.parameter == 0:
                kernel.remove()

        def simple_killer(kernel, process):
            process.parameter += 1

            if process.parameter == 2:
                kernel.kill_process(process.get_pid())

        kernel = kernel_t()
        
        kernel.create_process(process_t(
            "writer", 
            process_types_t.CONTINUOUS, 
            simple_writer, 
            0
        ))
        kernel.create_process(process_t(
            "killer", 
            process_types_t.CONTINUOUS, 
            simple_killer, 
            0
        ))
        kernel.create_process(process_t(
            "ender", 
            process_types_t.CONTINUOUS, 
            simple_ender, 
            4
        ))
        
        kernel.scheduler()


    def test_kernel_messages(self):

        def simple_sender(kernel, process):  
            print("Sender call")
            
            process.parameter += 1
            kernel.process_message_box_send("receiver", process.parameter)

        def simple_receiver(kernel, process):
            count = process.get_message_box().read()
            kernel.process_message_box_send("ender", count + 1)

        def simple_ender(kernel, process):
            count = process.get_message_box().read()
            print("Ender call: " + str(count))
            kernel.process_message_box_send("receiver", count + 1)

            if count > 15:
                kernel.remove()

        kernel = kernel_t()

        kernel.create_process(process_t(
            "sender",
            process_types_t.CONTINUOUS,
            simple_sender,
            0
        ))
        kernel.create_process(process_t(
            "receiver",
            process_types_t.REACTIVE,
            simple_receiver,
            0
        ))
        kernel.create_process(process_t(
            "ender",
            process_types_t.REACTIVE,
            simple_ender,
            0
        ))
        
        kernel.scheduler()

    
    def test_kernel_signal(self):
        def simple_alert_UwU(kernel, process):
            if process.get_message_box().read() != "UwU":
                return
            print("Received UwU signal!")

        def simple_alert_OwO(kernel, process):
            if process.get_message_box().read() != "OwO":
                return
            print("Received OwO signal!")
            kernel.process_message_box_send("ender", True)

        def simple_ender(kernel, process):
            if process.get_message_box().read():
                kernel.remove()

        def simple_trigger(kernel, process):
            print("Trigger run!")
            kernel.trigger_signal("OwO")
            kernel.trigger_signal("UwU")

        kernel = kernel_t()

        kernel.create_process(process_t(
            "uwu_signal",
            process_types_t.SIGNAL,
            simple_alert_UwU,
            0
        ))
        kernel.create_process(process_t(
            "owo_signal",
            process_types_t.SIGNAL,
            simple_alert_OwO,
            0
        ))
        kernel.create_process(process_t(
            "ender",
            process_types_t.REACTIVE,
            simple_ender,
            0
        ))
        kernel.create_process(process_t(
            "trigger",
            process_types_t.CONTINUOUS,
            simple_trigger,
            0
        ))

        kernel.scheduler()

if __name__ == "__main__":
    unittest.main()
