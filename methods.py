from bs4 import BeautifulSoup
from glob import glob
import os
from afinn import Afinn


def run_afinn(text):
    afinn = Afinn()
    return afinn.score(text)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    # [s.extract() for s in soup('script')]
    # TODO format the content
    return soup.get_text()


def visit_subdir(parent_dir):
    result = []
    for name in glob(parent_dir + "/*"):
        if os.path.isdir(name):
            result += visit_subdir(name)
        else:
            result.append(name)
    return result
