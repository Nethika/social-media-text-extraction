import spacy
import re,string
import random

# read name list from file
with open('names.txt') as f:
    names_list = f.readlines()
# remove whitespace characters like `\n` at the end of each line
names_list = [x.strip() for x in names_list] 
random.shuffle(names_list)



def remove_urls(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def remove_hashtags_handles(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)


def replace_names(input_text):
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(input_text)

    entities = []

    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.text not in entities:
            entities.append(ent.text)
        #if ent.label_ == 'PERSON':
            
    #print(entities)
    dict_entities = dict(zip(entities, names_list))
    print (dict_entities)
    for k,v in dict_entities.items():
        anonymous = input_text.replace(k, v)
    #print (anonymous)
    #print("")
    return anonymous

def preprocess_text(text):
    # Remove URLS
    prep_text = remove_urls(text)
    # Remove numbers
    # Remove Hashtags and Twitter handles
    prep_text = remove_hashtags_handles(prep_text)
    # Replace names
    prep_text = replace_names(prep_text)        
    # Lower case
    # Lemmatize
    return prep_text

