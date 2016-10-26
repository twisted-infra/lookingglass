import os
from os.path import expanduser
import socket

from twisted.application import service
from twisted.runner import procmon

import sys
from os.path import dirname
sys.path.insert(0, dirname(__file__))

from monitor import TracMonitor

TRAC_URL = 'http://127.0.0.1:9881/trac/'
TRAC_TIMEOUT = 30
CHECK_INTERVAL = 30

application = service.Application('trac')

# Setup trac server process monitor
processMonitor = procmon.ProcessMonitor()
processMonitor.addProcess('trac-server', [
    '/opt/trac/venv/bin/twistd',
    '--reactor', 'epoll',
    '--logfile', '/opt/trac/log/trac-twistd.log',
    '--pidfile', '/opt/trac/run/trac-twistd.pid',
    '--rundir', '/opt/trac/run/',
    '--python', '/opt/trac/trac_server.tac',
    '--nodaemon',
], env=os.environ)
processMonitor.setServiceParent(application)

def restartTrac():
    processMonitor.stopProcess('trac-server')

# Setup monitoring service
(TracMonitor(restartTrac, CHECK_INTERVAL, TRAC_URL, TRAC_TIMEOUT)
    .setServiceParent(application))
