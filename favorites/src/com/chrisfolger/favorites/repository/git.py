import subprocess
from subprocess import call
from subprocess import check_call
from subprocess import Popen
from subprocess import PIPE
import shlex
import os

logger = None

def set_logger(loggerObject):
    global logger
    logger = loggerObject

def git(command):
    logger.info(__name__, 'git', command)
    args = shlex.split('git '.join(command))
    p = Popen(args, stdout=PIPE, stderr=PIPE, bufsize=256*1024*1024)
    output, errors = p.communicate()
    return output, errors
    
def cd(directory):
    logger.info(__name__, 'cd', directory)
    os.chdir(directory)
    
def init_repo(directory):
    cd(directory)
    status()
    lg()

def status():
    git('status')

def lg():
    print git('lg --all')