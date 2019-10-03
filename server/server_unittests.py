import unittest
import pypackagereport

class pypackagereport_tests(unittest.TestCase):
    def testPyPackageComparison(self):
        # arrange
        package1 = pypackagereport.PyPackage("test", "v1.0", "na")
        package2 = pypackagereport.PyPackage("test", "v1.0", "na")
        package3 = pypackagereport.PyPackage("anothertest", "v1.0", "na")

        # act
        are_12_equal = package1 == package2
        are_13_equal = package1 == package3

        # assert
        self.assertTrue(are_12_equal)
        self.assertFalse(are_13_equal)


if __name__ == "__main__":
    unittest.main()