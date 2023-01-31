import unittest
import sys

sys.path.append("../src")
from aiko import process_t, process_types_t


class process_test_t(unittest.TestCase):

    def UwU(self, kernel, process):
        print("UwU")
        print(self.to_print)

        return process.parameter

    
    def test_create(self):
        process = process_t(
            "UwU_process", 
            process_types_t.REACTIVE, 
            self.UwU, 
            "OwO"
        )

        self.to_print = "XwX"

        self.assertEqual(
            process.get_pid(), 
            "UwU_process", 
            "Test process pid defined"
        )
        self.assertEqual(
            process.get_type(),
            process_types_t.REACTIVE,
            "Test process type defined"
        )
        self.assertEqual(
            process.worker(None, process),
            "OwO",
            "Test process worker and parameter work"
        )


    def test_message_box(self):
        process = process_t(
            "OwO_process",
            process_types_t.REACTIVE,
            self.UwU,
            "UwU"
        )

        self.assertEqual(
            process.get_message_box().is_readable(),
            False,
            "Test process message box"
        )

        process.get_message_box().send("UwU")

        self.assertEqual(
            process.get_message_box().read(),
            "UwU",
            "Trst process message box sending reading"
        )


if __name__ == "__main__":
    unittest.main()
