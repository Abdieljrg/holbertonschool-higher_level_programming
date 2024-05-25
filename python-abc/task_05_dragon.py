"""just random mixing"""


class SwimMixin:
    """mixin swimming ability."""

    def swim(self):
        """message the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """mixin flying ability."""

    def fly(self):
        """message the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class - dragon that swim and fly, from SwimMixin and FlyMixin."""

    def roar(self):
        """message the dragon roars."""
        print("The dragon roars!")
