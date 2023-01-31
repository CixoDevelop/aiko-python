import unittest
import sys

sys.path.append("../src")
from aiko import message_box_t


class message_box_test_t(unittest.TestCase):
    
    def test_create(self):
        message_box = message_box_t()

        self.assertEqual(
            message_box.read(), 
            None, 
            "Test message box create with blank message"
        )


    def test_send(self):
        message_box = message_box_t()
        
        elements = ["UwU", "OwO", "XwX"]

        for element in elements:
            message_box.send(element)

        self.assertEqual(
            message_box.is_readable(),
            True,
            "Testing readable detector, when data in message quere"
        )

        elements.reverse()

        for element in elements:
            self.assertEqual(
                message_box.read(),
                element,
                "Testing reading from message_box"
            )

        self.assertEqual(
            message_box.is_readable(),
            False,
            "Testing readable detector, when quere is blank"
        )


if __name__ == "__main__":
    unittest.main()
