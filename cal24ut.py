import unittest
import cal24op

class Cal24opTest(unittest.TestCase):
    def test_cal24_op_class(self):
        c1 = cal24op.Cal24op(1, 3, "+")
        c1.cal()
        self.assertEqual(c1.valid, True)
        c2 = cal24op.Cal24op(1, 3, "-")
        c2.cal()
        self.assertEqual(c2.valid, True)
        c3 = cal24op.Cal24op(1, 3, "*")
        c3.cal()
        self.assertEqual(c3.valid, True)
        c4 = cal24op.Cal24op(1, 3, "/")
        c4.cal()
        self.assertEqual(c4.valid, True)
        c5 = cal24op.Cal24op(0, 3, "/")
        c5.cal()
        self.assertEqual(c5.valid, True)
        c6 = cal24op.Cal24op(2, 3, "/")
        c6.cal()
        self.assertEqual(c6.valid, False)
        c7 = cal24op.Cal24op(0, 0, "/")
        c7.cal()
        self.assertEqual(c7.valid, False)

unittest.main()
