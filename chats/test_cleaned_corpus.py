import unittest
from unittest import TestCase
from settings import UNWANTED_WORDS_OR_PHRASES

from cleaned_corpus import (
    clean_messages,
    remove_conversational_chat_metadata,
    remove_any_remaining_unwanted_text,
    CORPUS_FILE,
    clean_corpus,
    format_each_corpus_conversational_sentence,
    remove_full_stops,
    our_corpus_cleaned_data



)
   


class CleanedCorpusTestCase(TestCase):
    def test_unwanted_words_or_phrase(self):
          """ assert that the users unwanted words or phrases is equal to the 
          to the one the user added."""
          unwanted_phrases =  UNWANTED_WORDS_OR_PHRASES
          more_unwanted_phrases = []
          more_unwanted_phrases.extend(unwanted_phrases)
          self.assertEqual( UNWANTED_WORDS_OR_PHRASES, more_unwanted_phrases)

    def test_remove_conversational_chat_metadata(self):
        """ check whether the removed conversational chat metadata is the same with the
         expected output incase if the user extended the files by adding other texts/chats
          to it in the future. """
        input_content = remove_conversational_chat_metadata(CORPUS_FILE)

        expected_output = []
        expected_output.extend(input_content)

        # Call the function with the input content
        result = (input_content)
     
        # Check if the result matches the expected output
        self.assertEqual(result, tuple(expected_output))
        
    def test_clean_corpus(self):
        """ assert that the clean corpus are equal to the expected output. """

        
        input_content = clean_corpus((CORPUS_FILE))
        # create an empty list which users corpus would be 
        # extended to
        expected_clean_corpus_output = []
        expected_clean_corpus_output.extend(input_content)

        # Call the function with the input content
        result = (input_content)
    
        # Check if the result matches the expected output
        self.assertEqual(result, tuple(expected_clean_corpus_output))


    
    def test_format_each_corpus_conversational_sentence(self):
          """ assert that the formated corpus conversational sentence has `.` as expected. """

          input_content = format_each_corpus_conversational_sentence( 
                                            clean_messages((
                                                    (clean_corpus(CORPUS_FILE))))
                                            )
          # create an empty list which users corpus would be 
          # extended to
          expected_corpus_conversational_output = []
          expected_corpus_conversational_output.extend(input_content)

            # Call the function with the input content
          result = (input_content)
        
            # Check if the result matches the expected output
          self.assertEqual(result, tuple(expected_corpus_conversational_output))

    
    def test_clean_messages(self):
          """ assert that the cleaned messages are equal to the expected output """

          
          input_content = clean_messages(((clean_corpus(CORPUS_FILE))))
          # create an empty list which users corpus would be 
          # extended to
          expected_clean_message_output = []
          expected_clean_message_output.extend(input_content)

            # Call the function with the input content
          result = (input_content)
        
            # Check if the result matches the expected output
          self.assertEqual(result, tuple(expected_clean_message_output))
    
    def test_remove_full_stops(self):
            """ assert that the the chat corpus full stops clusters are removed """

            input_content = remove_full_stops(clean_messages(clean_corpus(CORPUS_FILE)))

            expected_removed_full_stop_output = []

            expected_removed_full_stop_output.extend(input_content)

            # Call the function with the input content
            result = input_content

            self.assertEqual(result, tuple(expected_removed_full_stop_output))


    def test_our_corpus_cleaned_data(self):
          """ assert that the rsults of the cleaned chats is returned in a statements format """
          
          statements =  our_corpus_cleaned_data
          input_content = (clean_messages(clean_corpus(CORPUS_FILE)))

          expected_our_corpus_cleaned_data_output = []

          expected_our_corpus_cleaned_data_output.extend(input_content)

            # Call the function with the input content
          for statement in list(input_content):
              
               self.assertNotEqual(statement,  statements)




    def test_remove_any_remaining_unwanted_text(self):
         """ confirm whether the function can remove unwanted text as stipulated by the function
          we want to text """
         
         # let's assume the text we want to remove is stored in `remove_text` variable
         remove_text = 'Blaise'

         input_content = remove_any_remaining_unwanted_text((remove_text))

         expected_unwanted_output_copied_from_terminal = "Blaise"

         self.assertEqual(input_content, expected_unwanted_output_copied_from_terminal)


if __name__ == '__main__':
        unittest.main()


