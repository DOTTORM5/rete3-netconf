from ncclient import manager
import xml.dom.minidom
import my_xml

m = manager.connect(host="10.10.13.2", port=830, username="cisco", password="cisco", hostkey_verify=False)

#configurazione generale: hostname, nuovo username, password...
reply = m.edit_config(target="running", config=my_xml.config_global) 
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

#configurazione interfacce
reply = m.edit_config(target="running", config=my_xml.interface_confg)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

#configurazione OSPF
reply = m.edit_config(target="running", config=my_xml.ospf)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
