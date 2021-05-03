# OSPFv2 Remote Router Setup using NETCONF
- In `get-conf.py` we used the `ncclient` Python library to connect to a router in a star topology and setup OSPF routing on its interfaces.
- NETCONF XML commands were coded in Python strings in `my-xml.py` to set up:
  - Global configuration of the router
  - IP addressing on its `GigabitEthernet2` and `GigabitEthernet3` interfaces
  - OSPF routing on all `GigabitEthernet` interfaces
  - Passive interface on the `GigabitEthernet1` interface from which we access the topology
