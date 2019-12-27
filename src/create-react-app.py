import os
import sys
from lib import create_file
from pathlib import Path
import crap


if __name__ == "__main__":
    project_name = sys.argv[1]
    os.system('npx create-react-app ' + project_name)
    DIR_CURRENT_WORKING = Path.cwd()
    DIR_PROJECT_FOLDER = Path.joinpath(DIR_CURRENT_WORKING, project_name)
    DIR_PROJECT_SRC_FOLDER = Path.joinpath(DIR_PROJECT_FOLDER, 'src')
    DIR_PROJECT_PUBLIC_FOLDER = Path.joinpath(DIR_PROJECT_FOLDER, 'public')

    os.chdir(DIR_PROJECT_PUBLIC_FOLDER)
    crap.handle_index_html(DIR_PROJECT_PUBLIC_FOLDER, project_name)

    os.chdir(DIR_PROJECT_SRC_FOLDER)
    crap.remove_files()
    crap.create_app_jsx(DIR_PROJECT_SRC_FOLDER, project_name)
    crap.create_index_css(DIR_PROJECT_SRC_FOLDER)
    crap.create_empty_files(DIR_PROJECT_SRC_FOLDER, ['App.css'])

    os.chdir(DIR_PROJECT_FOLDER)
    crap.handle_readme_file(DIR_PROJECT_FOLDER, project_name)
    crap.create_empty_files(DIR_PROJECT_FOLDER, ['.env'])

    # Handle GIT
    os.system('echo ".env" >> .gitignore')
    os.system('git add .')
    os.system('git commit -m "removed crap files to empty project" ')

    os.system('code .')
    os.system('yarn start')
