class Fish:
    """A class representing a fish."""

    def swim(self):
        """fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """class bird."""

    def fly(self):
        """message bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """message (habitat) of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class flying fish (Fish and Bird.)"""

    def fly(self):
        """message the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """message the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """message the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
