class VerboseList(list):
    """ verboselist class adds messages for apend, extend, remove and pop."""
    def append(self, item):
        """ prints addition"""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """prints extention"""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """prints removed"""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        """prints pop"""
        if index is None:
            index = len(self) - 1
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
