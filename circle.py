from __future__ import annotations
import math


class Circle:

    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        :param radius: radius of the circle, may be zero.
        :raises ValueError: if radius is negative.
        """
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def add_area(self, circle: Circle) -> Circle:
        """Return a new circle whose area equals the combined
        area of this circle and another circle.
        Since area is pi*r**2, the radii of the 3 circles
        should form a Pythagorean triple (r1^2 + r2^2 = r3^2)

        >>> c1 = Circle(3)
        >>> c2 = Circle(4)
        >>> c1.add_area(c2)
        Circle(5.0)
        >>> c3 = Circle(-1)
        Traceback (most recent call last):
            ...
        """
        r1 = self.get_radius()
        r2 = circle.get_radius()
        r = math.hypot(r1, r2)
        return Circle(r)

    def get_area(self) -> float:
        """Return the area of the circle."""
        return math.pi*self.radius*self.radius
    
    def get_radius(self) -> float:
        """Return the radius of the circle."""
        return self.radius

    def __str__(self) -> str:
        """Return the string representation of the circle."""
        return f"Circle({self.radius})"
    
    __repr__ = __str__


if __name__ == "__main__":
    import doctest
    doctest.testmod()
