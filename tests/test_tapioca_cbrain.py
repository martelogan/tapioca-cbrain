# coding: utf-8

import unittest

from tapioca_cbrain import Cbrain


class TestTapiocaCbrain(unittest.TestCase):

    def setUp(self):
        self.wrapper = Cbrain()


if __name__ == '__main__':
    unittest.main()
