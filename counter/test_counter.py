"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
      
      def setUp(self):
         self.counter1 = Counter()
         self.counter2 = Counter()
       
      def test_singleton(self):
         """Verify that Counter is a singleton."""
         self.assertIs(self.counter1, self.counter2)
   
      def test_shared_count(self):
         """Verify that all instances share the same count."""
         self.counter1.reset()
         self.counter1.increment()
         self.assertEqual(self.counter2.count, 1)
   
      def test_count_not_reset(self):
         """Verify that the count is not reset to 0 
         when you invoke count = Counter() after the first time.
         """
         self.counter1.reset()
         self.counter1.increment()
         self.assertEqual(self.counter2.count, 1)

      def test_multiple_increment(self):
         """Verify that the count is not reset to 0 
         when you invoke count = Counter() after the first time.
         """
         self.counter1.reset()
         self.counter1.increment()
         self.counter2.increment()
         self.assertEqual(self.counter2.count, 2)
         self.assertEqual(self.counter1.count, 2)
