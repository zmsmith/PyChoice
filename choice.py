import random
import subprocess
import sys

def choose(choices):
    day_of_week = random.choice(choices)
    subprocess.call("say %s" % day_of_week, shell=True)
