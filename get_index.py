'''
Created on Dec 3, 2016

@author: oscar
'''
import os
import logging
from nltk.tokenize import word_tokenize
import methods
import collections
from collections import defaultdict
import json,sys

DYdictionary=defaultdict(list)


def add_to_dictionary(dictionary,term):
    dictionary[term] = []
    return dictionary[term]

def get_postings_list(dictionary,term): 
    return dictionary[term]
 
def add_to_postings_list(dictionary,term,path): 
    if path not in dictionary[term]:
        dictionary[term].append(path)
        
def IndexAllDept(root_dir_name='Departments'):
    root_dir = os.path.abspath(root_dir_name)
    if not os.path.exists(root_dir):
        logging.info("Root directory does not exist! (expected {})".format(root_dir_name))
        sys.exit(1)

    biology_dir = os.path.join(root_dir, 'biology')
    chemistry_dir = os.path.join(root_dir, 'chemistry')
    exercise_science_dir = os.path.join(root_dir, 'exercise-science')
    geography_planning_environment_dir = os.path.join(root_dir, 'geography-planning-environment')
    math_stats_dir = os.path.join(root_dir, 'math-stats')
    physics_dir = os.path.join(root_dir, 'physics')
    psychology_dir = os.path.join(root_dir, 'psychology')

    all_departments = [('Biology', biology_dir), ('Chemistry', chemistry_dir),
                            ('Exercise Science', exercise_science_dir),
                            ('Geography Planning Environment', geography_planning_environment_dir),
                            ('Math Stats', math_stats_dir), ('Physics', physics_dir), ('Psychology', psychology_dir)]

    [(dep_name, department_analysis(dep_dir, dep_name)) for dep_name, dep_dir in all_departments]
    '''
    [(dep_name, department_analysis(dep_dir, dep_name)) for dep_name, dep_dir in all_departments]
    sorted_x = collections.OrderedDict(sorted(DYdictionary.items()))        
    filestreamoutput=open("AllIndex.txt", "w")
    finaltext=unicode(json.dumps(sorted_x, ensure_ascii=False)).encode('utf-8')
    filestreamoutput.write(finaltext)
    filestreamoutput.close()
    DYdictionary.clear()
    print(dep_name+' finish')
    '''
def department_analysis(department_dir,dep_name):
    """
    Run sentiment analysis on a given department.
    :param department_dir: the directory containing all html files for the department.
    :return:
    """
    logging.info("Getting all html files for department dir {}".format(department_dir))
    html_files = methods.visit_subdir(department_dir)

    for f_path in html_files:
        with open(f_path) as f:
            f_content = f.read()
            logging.info("Parsing HTML & computing score for file {}".format(f_path))
        text = methods.parse_html(f_content)
        test_caseFolding=text.lower();
        """
        total_script_score += methods.run_afinn(text)
        
        tokens=word_tokenize(test_caseFolding)
        """
        path = f_path.replace("/Users/oscar/Desktop/project/COMP_479_FINAL_PROJECT/index/", "")
        tokens=word_tokenize(test_caseFolding)
        if len(tokens)==0:
                break
        else:
            for index in range(len(tokens)):
                temp=tokens[index]
                if temp not in DYdictionary:
                    add_to_dictionary(DYdictionary,temp)
                else:
                    get_postings_list(DYdictionary,temp)
                add_to_postings_list(DYdictionary,temp,path)
        
    sorted_x = collections.OrderedDict(sorted(DYdictionary.items()))        
    filestreamoutput=open(dep_name+".txt", "w")
    finaltext=unicode(json.dumps(sorted_x, ensure_ascii=False)).encode('utf-8')
    filestreamoutput.write(finaltext)
    filestreamoutput.close()
    print(dep_name+' finishes. And there are '+ str(len(DYdictionary))+" of tokens.")
    DYdictionary.clear()

if __name__ == '__main__':
    IndexAllDept()
    