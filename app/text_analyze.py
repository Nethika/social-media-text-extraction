import spacy
import textacy
import textacy.lexicon_methods


def emotion_values(input_text):
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(input_text)

    return textacy.lexicon_methods.emotional_valence(doc)