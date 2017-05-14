# coding:utf-8
from pysnmp.entity.rfc3413.oneliner import cmdgen
import re
cmdGen = cmdgen.CommandGenerator()
import time
def getTrunk(ip, port, agent, communication,oid):
    gen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = gen.nextCmd(
        cmdgen.CommunityData(agent, communication, 1),
        cmdgen.UdpTransportTarget((ip, port)),
        oid,
    )
    patter = re.compile('=(.*)')
    cdp_list = []
    for bind in varBinds:
        for i in bind:
            i = str(i)
            cdp_list.append(patter.findall(i))

    print " 总数量为：  %s " % len(cdp_list)
    print '具体如下：'
    for i in cdp_list:
        print i

    # return errorIndication, errorStatus, errorIndex, varBinds


oid = (1,3,6,1,4,1,9,9,23,1,2,1,1,7)
getTrunk('xx.xx.xx.xx', 161, 'public', 'public',oid)

time.sleep(4)

print '---------- CDN 邻居地址：：：：：：：：：'
oid1 = (1,3,6,1,4,1,9,9,23,1,2,1,1,6)
getTrunk('xx.xx.xx.xx', 161, 'public', 'public',oid1)
time.sleep(4)

print '---------- 接口地址：：：：：：：：：'

oid2=(1,3,6,1,2,1,4,20,1,1)
getTrunk('xx.xx.xx.xx', 161, 'public', 'public',oid2)





