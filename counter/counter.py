"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""

class Counter:
    def __new__(cls):
        """Create a single instance of the class."""
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the counter to zero."""
        if not hasattr(self, "_count"):
            self._count = 0

    def __str__(self):
        """Return the current count as a string."""
        return f"{self._count}"

    @property
    def count(self):
        """Return the current count."""
        return self._count
    
    def increment(self):
        """Increment the count by 1."""
        self._count += 1
        return self._count

    def reset(self):
        """Reset the count to zero."""
        self._count = 0