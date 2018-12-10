import unittest

import app


class MyTestCase(unittest.TestCase):
    def testSearch(self):
        data = [(1, "", "tour city",), (2, "", "some other",)]
        db = app.DB(entries=data)
        self.assertEqual(db.search("city tour"), [(1, '', 'tour city')])


if __name__ == '__main__':
    unittest.main()
