#! /usr/bin/env python

#################################################
# Author , Vishal Jagtap
# URL Data
#
# 2016-02-18     v1.0     : Initial release
# 2016-03-22     v1.2     : Added mongoDB driver and module
#################################################

import sys
import logging
import inspect
import re



def logit(scriptname, mode, msg, level, ln):
    logfile = re.sub('.py', '.log', scriptname)
    logfile = "/devops1/devtools/logs" + logfile
    print logfile
    msg = '(%d) %s' % (ln, msg)  # interpolation to print line number of code where error occured
    format1 = '%(asctime)s [%(levelname)s] %(message)s'
    format2 = '%(asctime)s [%(levelname)s] [%(filename)s , %(funcName)s , %(module)s] %(message)s'
    if mode == "d":
        logging.basicConfig(filename=logfile, format=format2, level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S %p')
    elif mode == "n":
        logging.basicConfig(filename=logfile, format=format1, level=logging.INFO, datefmt='%Y-%m-%d %I:%M:%S %p')
    else:
        logging.basicConfig(filename=logfile, format=format1, level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S %p')

    if level == "I":
        logging.info(msg)
    elif level == "W":
        logging.warning(msg)
    elif level == "E":
        logging.error(msg)
    elif level == "C":
        logging.critical(msg)