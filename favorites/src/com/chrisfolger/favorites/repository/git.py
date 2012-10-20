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
    args = shlex.split(command)
    args.insert(0, 'git')
    p = Popen(args, stdout=PIPE, stderr=PIPE, bufsize=256*1024*1024)
    output, errors = p.communicate()
    logger.color(__name__, ' '.join(args), 'blue', output, errors)
    return output, errors
    
def cd(directory):
    logger.info(__name__, 'cd', directory)
    os.chdir(directory)
    
def init_repo(directory):
    logger.info(__name__, 'init_repo', directory)
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
    logger.info(__name__, 'makedir', dir)
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
    return git('commit -m "' + message + '"')