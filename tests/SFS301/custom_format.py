"""Example of f-string with custom format method."""


class Client:
    """Customer or client object."""

    def __init__(self, id, polite, casual):
        """Initialise the class."""
        self.polite = polite
        self.casual = casual

    def __format__(self, format_spec):
        """Support format method or f-string."""
        if format_spec == "polite":
            return self.polite
        elif format_spec == "casual":
            return self.casual
        else:
            # Using string addition here to avoid triggering flake8-sfs
            # while still giving a meaningful self-contained example:
            raise ValueError(format_spec + " not a format defined by Client object")


customer = Client(123, "Peter", "Pete")

print(f"Hello {customer:polite}, may we call you {customer:casual}?")
