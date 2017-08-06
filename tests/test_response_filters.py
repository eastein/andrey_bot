import unittest

import andrey_bot.filtering

class TestWordFilter(unittest.TestCase):
    def test_simple_word_filter(self):
        wf = andrey_bot.filtering.WordFilter(['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
        # TODO this assertion should fail if the scunthorpe problem is fixed
        self.assertTrue(wf.acceptance_test('Some foxes are quick.'))
        # some straightforward assertions
        self.assertTrue(wf.acceptance_test('The dog jumps.'))
        self.assertFalse(wf.acceptance_test('Clocks!'))

class TestNotImplemented(unittest.TestCase):
    def test_not_use_base(self):
        bci = andrey_bot.filtering.Filter()
        self.assertRaises(NotImplementedError, bci.acceptance_test, 'hi')