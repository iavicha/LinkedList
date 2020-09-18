import unittest
from linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append(1)
        self.assertEqual(self.linked_list._LinkedList__head.value, 1)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 1)
        self.assertEqual(len(self.linked_list),1)

        # добавление в пустой список


    def test_iter(self):

        for value in values
        self.linked_list.append(1)
        self.linked_list.append(2)



if __name__ == '__main__':
    unittest.main()
