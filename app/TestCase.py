class DB(object):
    def __init__(self, entries=None):
        self.entries = [] if entries is None else entries

    def add(self, entry):
        """An entry is a tuple of (id, datetime, text)."""
        self.entries.append(entry)

    def search(self, query_string):
        """
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).search("city tour")
        [(1, '', 'tour city')]
        """
        result = self.entries
        for item in set(query_string.split()):
            result = filter(lambda x: item in x[2], result)
        return list(result)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
