
################################################################################
# SETUP                                                                        #
# -------------------------------------------------------------------          #
# mininet:  mininet.sh --topo single,3                                         #
# test:     pingall and check for following connectivity pattern               #
#           h1 -> h2 h3                                                        # 
#           h2 -> X h3                                                         #
#           h3 -> X h2                                                         #
#           all hosts should also be able to ping 10.0.0.11                    #
################################################################################

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *


ip1 = IPAddr('10.0.0.1')
ip2 = IPAddr('10.0.0.2')
ip3 = IPAddr('10.0.0.3')

l3route = ((match(dstip=ip1) >> fwd(1)) +
           (match(dstip=ip2) >> fwd(2)) +
           (match(dstip=ip3) >> fwd(3)) )

def main():
    return policy




