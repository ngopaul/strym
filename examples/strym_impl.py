#!/usr/bin/env python
# coding: utf-8

# Author : Rahul Bhadani
# Initial Date: Nov 11, 2019

from strym import strym
import cantools
import sys, math, time
import signal
import subprocess, shlex
from subprocess import call
import psutil
import glob
import os

db = './newToyotacode.dbc'

Viz = strym(dbcfile = db)

message_type_to_visualize = 'SPEED'
message_attribute_number_to_visualize = 1

visualize = False
options = {"log": "info" }
Viz.isolog(visualize, message_type_to_visualize, message_attribute_number_to_visualize,  **options)

signal.signal(signal.SIGINT, Viz.kill)

print('Datafile saved is {}'.format(Viz.logfile))