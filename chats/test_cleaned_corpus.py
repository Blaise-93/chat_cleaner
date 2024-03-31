import unittest
from unittest import TestCase
from settings import UNWANTED_WORDS_OR_PHRASES

from cleaned_corpus import (
    clean_messages,
    cleaned_tuple,
    remove_any_remaining_unwanted_text,
    CORPUS_FILE,
    format_each_corpus_conversational_sentence

)



class CleanedCorpusTestCase(TestCase):
    def test_unwanted_words_or_phrase(self):
          """ assert that the users unwanted words or phrases is equal to the 
          to the one the user added."""
          unwanted_phrases = UNWANTED_WORDS_OR_PHRASES
          p = more_unwanted_phrases = []
          more_unwanted_phrases.extend(unwanted_phrases)
          print(p)
          self.assertEqual(UNWANTED_WORDS_OR_PHRASES, more_unwanted_phrases)

    

 





if __name__ == '__main__':
        unittest.main()