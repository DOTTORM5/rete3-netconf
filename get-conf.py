from ncclient import manager
import xml.dom.minidom
import my_xml

m = manager.connect(host="10.10.13.2", port=830, username="cisco", password="cisco", hostkey_verify=False)


reply = m.edit_config(target="running", config=my_xml.ospf)
# reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

