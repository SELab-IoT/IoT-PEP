#-*- coding: utf-8 -*-

from application import app

import application.access_control
import application.device_registration
import application.login
from util import profile_manager

import json

print("Load PEP Profile")
profile_manager.loadProfile()
pep_profile = profile_manager.getProfileAsDict()
host_ip, host_port = pep_profile["pepIp"].split(":")

print("PEP Server Starting...\n")
app.run(host=host_ip, port=int(host_port), debug=True)

