import unittest
import swick


class TestReadSWC(unittest.TestCase):

    def test_too_few_fields(self):
        with self.assertRaises(swick.SWCFormatError):
            swick.read_swc('test/data/too_few_fields.swc')

    def test_too_many_fields(self):
        with self.assertRaises(swick.SWCFormatError):
            swick.read_swc('test/data/too_many_fields.swc')


if __name__ == '__main__':
    unittest.main()
