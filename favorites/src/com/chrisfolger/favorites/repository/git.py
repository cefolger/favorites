import subprocess
from subprocess import Popen
from subprocess import PIPE
import shlex
import os

repositoryDoesntExist = 'fatal: Not a git repository (or any of the parent directories): .git\n'
logger = None

def set_logger(loggerObject):
    global logger
    logger = loggerObject

def git(command):
    args = shlex.split(command.encode('ascii','ignore'))
    args.insert(0, 'git')
    p = Popen(args, stdout=PIPE, stderr=PIPE, bufsize=256*1024*1024)
    output, errors = p.communicate()
    logger.color(__name__, ' '.join(args), 'blue', output, errors)
    return output, errors
    
def cd(directory):
    logger.color(__name__, 'cd', 'blue', directory)
    os.chdir(directory)
    
def init_repo(directory):
    logger.color(__name__, 'init_repo', 'blue', directory)
    cd(directory)
    output, errors = status()
    if(errors == repositoryDoesntExist):
        # good to go, create the repository
        # after creation, create the folder
        logger.info(__name__, 'init repo', 'repository doesnt exist, creating it...')
        git('init')
        makedir('favorites')
        add()
        commit('initial repo creation')
        return True
    logger.warn(__name__, 'init repo', 'repository present, ignoring')
    return False 
        
def makedir(dir):
    logger.color(__name__, 'makedir', 'blue', dir)
    os.makedirs(dir)
    file = open(dir + '/blank', 'w+')

def status():
    return git('status')

def changesExist():
    return git('status --porcelain') != ('', '')

def lg():
    return git('lg --all')

def add(options = ''):
    return git('add . ' + options)

def commit(message):
    return git(r'commit -m "' + message + '"')

def get_commits():
    output, errors = git('log --pretty=oneline --abbrev-commit')
    print output
    
    return output

def rollback():
    return git('reset --hard HEAD~1')