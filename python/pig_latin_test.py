# Rewrite this in Unit Test


from pig_latin import translate


import unittest

class PigLatinTest(unittest.TestCase):
  def test_return(self):
    """test return of function"""
    self.assertIsNotNone(translate('apple'))
    
  def test_simple_1(self):
    """simple test case"""
    self.assertEqual(translate('apple'), 'appleay')

  def test_simple_2(self):
    """simple test case"""
    self.assertEqual(translate('banana'), 'ananabay')

  def test_complex_1(self):
    """more than 1 consonant"""
    self.assertEqual(translate('cherry'), 'errychay')

  def test_complex_2(self):
    self.assertEqual(translate('eat pie'), 'eatay iepay')

  def test_complex_3(self):
    self.assertEqual(translate('three'), 'eethray')

  def test_complex_4(self):
    self.assertEqual(translate('school'), 'oolschay')

  def test_complex_5(self):
    self.assertEqual(translate('quiet'), 'ietquay')

  def test_complex_6(self):
    self.assertEqual(translate('the quick brown fox'), 'ethay ickquay ownbray oxfay')

  def test_complex_7(self):
    self.assertEqual(translate('The quick brown Fox'), 'Ethay ickquay ownbray Oxfay')

  def test_complex_8(self):
    self.assertEqual(translate('The quick, brown Fox.'), 'Ethay ickquay, ownbray Oxfay.')

if __name__ == "__main__":
  unittest.main()

# write a test asserting that capitalized words are still capitalized
# (but with a different initial capital letter, of course) retain the
# punctuation from the original phrase
