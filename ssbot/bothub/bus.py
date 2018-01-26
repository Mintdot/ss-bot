# -*- coding: utf-8 -*-

import urllib.request
from xml.dom import minidom


def bus_response(data):
    id = data
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=umfGiqjtzOMarryKchlVrnqw7%2BGPqeV1bDPWigHtwAFpAB8d5lfQ8TXoBvRDCRecXTrmkbz24APGWQR0kPY3Ow%3D%3D&arsId={}'.format(id)
    data = urllib.request.urlopen(url).read()
    xml_file = "test.xml"
    f = open(xml_file, "wb")
    f.write(data)
    f.close()
    xml_doc = minidom.parse('test.xml')
    item_list = xml_doc.getElementsByTagName('itemList')
    item = item_list[0].getElementsByTagName('arrmsg1')
    res = item[0].firstChild.data

    return res
