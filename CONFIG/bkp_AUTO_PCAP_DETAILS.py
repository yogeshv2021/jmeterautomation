#####Alias of the Server which is used as center for all PCAP Validations##############
PCAP_SERVER_ALIAS = [ "117_SERVER"]

PCAP_STRING = [ "/usr/sbin/dumpcap -i eth0 eth0:4020 -i eth0:4021 -i lo:8400  -s 65535 -a duration:200" ]

PCAP_XML_CONVERSION_STRING = [ "/usr/sbin/tshark -n -o xml.tcp.port:\"8400\" -o http.tcp.port:\"4020,4021\" ", "/usr/local/bin/tshark -n" ]

PCAP_XML_CONVERSION_END_STRING = [ "-T fields -e data-text-lines -e xml.tag -e xml.unknown -e xml.cdata -e xml.cdatasection -e xml.closing_unopened_tag -e xml.comment -e xml.doctype -e xml.xmlpi -e xml.dtdtag | awk 'NF'","-T pdml | egrep -i \'gsm_|camel.|inap.|USSD\'" ]

PCAP_CAPTURE_REMOTE_PATH = [ "/opt/product/testteam/Products/AUTOMATION/NIG/PCAP/" ]

PCAP_VALIDATION_INPUT_ALIAS= [ "NIG" ]

##### Grep Type=1 default 2 for NIG Product##############
PCAP_GREP_TYPE= 2