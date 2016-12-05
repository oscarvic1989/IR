from bs4 import BeautifulSoup
from glob import glob
import os
import math
from afinn import Afinn
from nltk.tokenize import word_tokenize


def run_afinn(text):
    afinn = Afinn()
    return afinn.score(text)


def sentiment(doc_string):
    """ Computes the sentiment score for a given document """
    afinn_score = run_afinn(doc_string)
    return afinn_score if afinn_score else 0


def sentiment_score(doc_string):
    """ Computes the normalized sentiment score for a given document string """
    token_count = len(word_tokenize(doc_string))
    scale_factor = 100
    r1 = sentiment(doc_string)
    return float(r1 * scale_factor) / math.sqrt(token_count)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def visit_subdir(parent_dir):
    result = []
    for name in glob(parent_dir + "/*"):
        if os.path.isdir(name):
            result += visit_subdir(name)
        else:
            result.append(name)
    return result
