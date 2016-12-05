#!/usr/bin/env python2

import os
import sys
import logging
from tabulate import tabulate

import methods


def full_analysis(root_dir_name='Departments'):
    """
    Run sentiment analysis on all the departments.
    :param root_dir_name: the name of the root directory where to look for the department directories.
    :return the resulting anaylsis scores.
    """
    _setup_log()

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

    department_results = [(dep_name, department_analysis(dep_dir)) for dep_name, dep_dir in all_departments]
    print_results(department_results)

    return department_results


def print_results(department_results):
    """
    Print the results of the given sentiment analysis.
    :param department_results: a list of tuples of the form (department_name, department_sentiment_score).
    """
    logging.info("\n")
    logging.info("Results:")

    headers = ['Departments', 'Sentiment Score']
    data = [[dep_name, dep_score] for dep_name, dep_score in department_results]

    logging.info(tabulate(data, headers=headers, tablefmt='grid'))


def department_analysis(department_dir):
    """
    Run sentiment analysis on a given department.
    :param department_dir: the directory containing all html files for the department.
    :return:
    """
    logging.info("Getting all html files for department dir {}".format(department_dir))
    html_files = methods.visit_subdir(department_dir)

    total_script_score = 0

    for f_path in html_files:
        with open(f_path) as f:
            f_content = f.read()
            logging.info("Parsing HTML & computing score for file {}".format(f_path))
        text = methods.parse_html(f_content).lower()
        total_script_score += methods.sentiment_score(text)

    total_script_score /= len(html_files)

    logging.info("Total score for department: {}".format(total_script_score))

    return total_script_score


def _setup_log():
    """
    Setup the log.
    """
    log_file = 'analysis.log'
    if os.path.exists(log_file):
        os.remove(log_file)

    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m-%d %H:%M')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    full_analysis()
