import random
import subprocess
import sys
from optparse import OptionParser

def choose():    
    parser = OptionParser()
    opts, args = parser.parse_args()
    
    
    day_of_week = random.choice(args)
    subprocess.call("say %s" % day_of_week, shell=True)
