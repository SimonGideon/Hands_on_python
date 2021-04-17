import datetime
import os
from lib2to3.pgen2 import conv

os.getcwd()  # returns the current directory
os.chdir('D:\DESKTOP')  # changes the  directory
os.system('mkdir today')  # Run the cmd mkdir in the system shell

import os

dir(os)
help(os)  # help
import shutil

shutil.copyfile('data.db', 'archive.db')
shutil.move('/bulid/executables', 'installer')

# FIle_wildcards
import glob

glob.glob('*py')

# Command_line_argument
import sys

print(sys.argv)

# Error_output_redirection_and_program_termination
sys.stderr.write('warning, log file not found starting a new one\n')

# string_pattern_matching
import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z)+) \1' r'\1', 'cat in the hat')

# Mathematics
import math

math.cos(math.pi / 4)

math.log(1024, 2)
import random

random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)  # sampling without replacement

random.random()  # random float
random.randrange(6)
# statistical_analysis_and_data
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.variance(data)

# Internet_access
from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('netflixblackbelt@gmail.com', 'simongideon918@gmail.com',
                """To: simongideon918@gmail.com
From: Balckbeltnetflix@gmail.com
            
Is time to rock it out.
""")
server.quit()

# Date_and_time
from datetime import date

now = date.today()
now
datetime.date(2003, 12, 2)
now.stftime("%m-%d-%y. %d%b%y is a %A on the %d day of %B.")

# date also supports callendar arithmentic
birthday = date(1964, 7, 31)
age = now - birthday
age.day

# Date_compression
import zlib

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# Performance_management
from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# Quality_Control
def average(value):
    """Computes the arithmetic mean of a list of numbers.
    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest
doctest.testmod() # automatically validate the embedded tests

import unittest


def avarage(param, param1, param2):
    pass


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            avarage(20, 30, 70)


unittest.main()  # calling from the command line invokes all lines

# Output_fommating
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))

import pprint
t = [[[['black', 'cyan',], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow']
  'blue']]]
import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of stringsinstead of one
big strings with newlines to separate the wrapped lines."""
print(textwrap.fill(doc, width=40))
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

cov = locale.localeconv()
x = 1234567.8
locale.format_string("%s%.*f", (conv['currency_symbol'],
                                cov['frac_digits'], x), grouping=True)

# Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

# Working_binary_data_record_layout
import struct
with open('myfile.zip', 'rib') as f:
    data = f.read()
    
start = 0
for i in range(3):
    start += 14
    fields =struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start+extra_size]
    print(filename, hex(crc32), comp_size,uncomp_size)
    start += extra_size + comp_size   # skip to the header.

# Multi-threading
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = ooutfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIPfile.ZIP_DEFlated)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()    # wait for the background task to finish
print('Main program waited until background was done.')




# Logging
import logging
logging.deburg('Debugging information')
logging.info('Informal message')
logging.warning('warning:config file % not found', 'server.conf')
logging.warning('Error occurred')
logging.critical('Critical erro -- shutting down')

# Weak_refernce
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)    # create a reference
d = weakref.weakValueDictionary()
d['primary'] = a    # Does not creat a reference
d['primary']        # fetch the object if ti is still a live

del a       # remove the on reference
gc. collected()    # returns the gabage collector right away
d['primary']    # entry was automatically removed



# Tools_for_working_with_list
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
a[1:3]
 from collections import deque
 d = deque(["task1","task2", "task3"])
 d.append("Handling", d.popleft())


def starting_model(args):
    pass


unsearched = deque([starting_model])
 def is_goal(m):
     pass


def breadth_first_search(unsearched):
     mode = unsearched.popleft()
     for m in gen_move(node):
         if is_goal(m):
             return m
         unsearched.append(m)
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1, 3,  5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)    # rearrange the list to heap order
heappush(data,-5)    # add a new entry
[heappop(data) for i in range(3)]    # fetch the three smallest entries

# Decimal_floating_point_arithmetic
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
round(.70 * 1.05, 2)

Decimal('1.00') % Decimal('.10')

1.00 % 0.10

sum([Decimal('0.1')]*10) ==Decimal('1.0')

sum([0.1]*10) == 1.0



    
