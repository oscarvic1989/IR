#!/usr/bin/env python2

import os

root_dir = os.path.abspath('Departments')

biology = ('http://www.concordia.ca/artsci/biology.html', os.path.join(root_dir, 'biology'))
chemistry = ('http://www.concordia.ca/artsci/chemistry.html', os.path.join(root_dir, 'chemistry'))
exercise_science = ('http://www.concordia.ca/artsci/exercise-science.html', os.path.join(root_dir, 'exercise-science'))
geography_planning_environment = ('http://www.concordia.ca/artsci/geography-planning-environment.html', os.path.join(root_dir, 'geography-planning-environment'))
math_stats = ('http://www.concordia.ca/artsci/math-stats.html', os.path.join(root_dir, 'math-stats'))
physics = ('http://www.concordia.ca/artsci/physics.html', os.path.join(root_dir, 'physics'))
psychology = ('http://www.concordia.ca/artsci/psychology.html', os.path.join(root_dir, 'psychology'))

departments = [biology, chemistry, exercise_science, geography_planning_environment, math_stats, physics, psychology]


def make_dirs(dep_dir):
    if not os.path.exists(dep_dir):
        os.makedirs(dep_dir)


def main():
    for dep_url, dep_dir in departments:
        make_dirs(dep_dir)
        print(dep_dir)
        os.system('cd {} && wget -r -np -nH --follow-tags=a --cut-dirs=3 -R index.html {}'.format(dep_dir, dep_url))


if __name__ == '__main__':
    main()
