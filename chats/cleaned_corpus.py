import re


def remove_conversational_chat_metadata(chat_export_file):
    """ a function that removes imported unused data like date_time, dash_whitespace,
     username, and metadata end to facilitate in corpus bot training (for the company info)."""
    
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "1/16/24, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    corpus_username = r"([\w\s]+)"  # e.g. "Eches"
    metadata = r":\s"  # ": "
    #pattern = r'^[a-zA-Z\s]+$'
    pattern = date_time + dash_whitespace + corpus_username + metadata

    try:
        with open(chat_export_file, "r", encoding="utf-8") as corpus_file:
            content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n"))
    
    except UnicodeDecodeError:
        print(f"Error reading file {chat_export_file}.")

def clean_corpus(chat_export_file):
    """ clean corpus to bearest minimum  """
    message_corpus = remove_conversational_chat_metadata(chat_export_file) 
    return message_corpus


def ends_with_period_or_question_or_excl(sentence):
    return sentence.endswith('.') or sentence.endswith('?') \
        or sentence.endswith("!")


def format_each_corpus_conversational_sentence(sentence):
    """
    Format the generated corpus conversation sentence by appending '.' to 
    the last statement in the chat if it was not attached by the user prior to 
    manipulating the chat logs via regex. You can actually disable this function
    if you don't want it, once you allow it, it will auto-add the fullstop to
    any of the sentence that doesn't have fullstop.
    """
    sentences = []
    for statement in sentence:
        formatted_sentence = statement.capitalize()
        # Append "." if it's not already there
        if not ends_with_period_or_question_or_excl(formatted_sentence):
            formatted_sentence += "."
        sentences.append(formatted_sentence)
    return tuple(sentences)

# Example usage
input_sentences = ["I love Blaise", "Blaise love Python", "Blaise has been writing Python code since 2019"]
formatted_result = format_each_corpus_conversational_sentence(input_sentences)
#print(formatted_result)

def clean_messages(messages):
    """ helps us remove emojis, media omitted times, names and times which 
        is attached when the log chats is generated from clean_corpus via 
        usage of regex methods.

        ::  returns a tuple.
     """
    
    cleaned_messages = []
    for message in messages:

        # Remove dates, media omitted, times, names, hyphens, and emojis
        cleaned = re.sub(r'<Media omitted>|\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\u202f[APM]{2} - \w+: ', '', message)
        
        # comment the below line of code if you want to make use of emojis of all types
        # once it is commented with "#" it will definitely allow emojis visibility.
        cleaned = re.sub(r'[\U00010000-\U0010ffff]', '', cleaned)

        cleaned = re.sub(r'-', '', cleaned)
        cleaned_messages.append(cleaned)
    return tuple(cleaned_messages)


def remove_any_remaining_unwanted_text(text):
    """ Define patterns to match dates and unwanted phrases that are most likely going to pop out.
    Add any further inconsistence/impurities to the `unwanted_phrase` variable which is a list by copy
    and paste from your terminal."""
    date_pattern = r'(\d+\/\d+\/\d+,\s\d+:\d+)'

    # add any unwanted phrase here in the list as a string from your printed tuple on your cmd,
    #  mine might definitely be different from yours, only if you are using the same chats.txt
    # files as mine.
    unwanted_phrases = [
            'pharm chinyere _ nett pharmacy','pm', "am", ":", '\u200d♂',
            "px king cj",

        ]

    # Remove dates
    text = re.sub(date_pattern, '', text)

    # Remove unwanted phrases
    for phrase in unwanted_phrases:
        text = text.replace(phrase, '')

    # Remove extra spaces
    text = ' '.join(text.split())

    return text



def remove_full_stops(messages):
    cleaned_messages = tuple([re.sub(r'\.', '', msg) for msg in messages])
    return cleaned_messages


# Clean the messages and print the result
CORPUS_FILE = 'chats/chats.txt'
cleaned_tuple = format_each_corpus_conversational_sentence(
                            clean_messages((
                               (clean_corpus(CORPUS_FILE))))
                           )

# Remove unwanted text from each element of the tuple
cleaned_messages = tuple(remove_any_remaining_unwanted_text(text) for text in cleaned_tuple)
print(cleaned_messages)

def our_corpus_cleaned_data():
    """ this function returns strings of the chat corpus of the `cleaned_messages` when 
    run. Once you call up the function by uncommenting the `our_corpus_cleaned_data` you
    will see it in action."""
    for chats in list(cleaned_messages):
        print(chats)
    

#our_corpus_cleaned_data()

# NB: You can import cleaned_messages our_corpus_cleaned_data() in any of your python
# scripts and use it for your further data cleaning.
