import unittest
from binary_search_tree import BST
from AVL_tree import AVLTree
from red_black_tree import RedBlackTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_insert_and_search(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.assertIsNotNone(self.bst.search(10))
        self.assertIsNotNone(self.bst.search(5))
        self.assertIsNone(self.bst.search(15))  # Check for non-existent element

    def test_delete(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.delete(10)
        self.assertIsNone(self.bst.search(10))

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def test_insert_and_search(self):
        self.avl.insert(10)
        self.avl.insert(5)
        self.avl.insert(20)
        self.assertIsNotNone(self.avl.root)
        self.assertEqual(self.avl.root.key, 10)  # Verify root after insertion
        self.assertIsNotNone(self.avl.search(20))
        self.assertIsNone(self.avl.search(30))  # Check for non-existent element

    def test_delete(self):
        self.avl.insert(10)
        self.avl.insert(5)
        self.avl.insert(20)
        self.avl.delete(10)
        self.assertIsNone(self.avl.search(10))  # Check deletion
        self.assertIsNotNone(self.avl.search(5))  # Other elements intact

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.rbt = RedBlackTree()

    def test_insert_and_search(self):
        self.rbt.insert(10)
        self.rbt.insert(5)
        self.rbt.insert(20)
        self.assertIsNotNone(self.rbt.search(10))
        self.assertIsNotNone(self.rbt.search(5))
        self.assertIsNone(self.rbt.search(15))  # Check for non-existent element

    def test_delete(self):
        self.rbt.insert(10)
        self.rbt.insert(5)
        self.rbt.insert(20)
        self.rbt.delete(10)
        self.assertIsNone(self.rbt.search(10))  # Check deletion
        self.assertIsNotNone(self.rbt.search(5))  # Other elements intact

if __name__ == "__main__":
    unittest.main()
