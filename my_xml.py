

# questo script xml  andra a settare i seguenti parametri all'interno del nostro router csr1000kv.

#### IN COONFIG-GLOBAL ANDRA' AD IMPOSTARE I SEGUENTI PARAMETRI######
# BANNER
# PASSWORD-ENCYPTION
# HOSTNAME 
# USERNAME
# SECRET-PASSWORD
#-----------------------------------------------------------

config_global="""
<config>
   <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <banner>
        <motd>
          <banner>FUORI DAI PIEDI!!!</banner>
         </motd>
      </banner>
       
      <service>
         <password-encryption/>
      </service>
      
      <hostname>TEAM3</hostname>
      <username>
            <name>Team3</name>
            <secret>
                <secret>cisco</secret>
            </secret> 
      </username>
        <line>
         <console>
          <first>0</first>
           <password>
             <secret>cisco</secret>
           </password>
             <stopbits>1</stopbits>
         </console> 
        </line>
   </native>
</config>"""


#### IN INTERFACE-CONFIG ANDRA' AD IMPOSTARE I SEGUENTI PARAMETRI######
# INDIRIZZI IP SULLE INTERFACCE GigabitEthernet1 E GigabitEthernet2
#-----------------------------------------------------------

interface_confg = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
               <name>2</name>
                 <description>gigabit ethernet 2</description>
                   <ip>
                    <address>
                       <primary>
                         <address>10.10.22.2</address>
                         <mask>255.255.255.252</mask>
                       </primary>
                    </address>
                   </ip>
            </GigabitEthernet>
        </interface>
        <interface>
          <GigabitEthernet>
            <name>3</name>
              <description>gigabit ethernet 3</description>
                <ip> 
                  <address>
                    <primary>
                       <address>10.10.23.1</address>
                       <mask>255.255.255.252</mask>
                    </primary>
                  </address>
               </ip>                       
          </GigabitEthernet>
        </interface>
    </native>
</config>"""




#### IN OSPF ANDRA' AD IMPOSTARE I SEGUENTI PARAMETRI######
# OSPF SU TUTTE LE INTERFACCE
# PASSIVE INTERFACE GigabitEthernet1
#-----------------------------------------------------------

ospf = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <router>      
   <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
     <ospf>
        <process-id>
           <id>10</id>
              <passive-interface>
                <interface>GigabitEthernet1</interface>
                  </passive-interface>
                  
               <router-id>3.3.3.3</router-id>
            
                     <network>
                        <ip>10.10.13.0</ip>
                        <wildcard>0.0.0.3</wildcard>
                        <area>0</area>
                     </network>
             
                     <network>
                        <ip>10.10.22.0</ip>
                        <wildcard>0.0.0.3</wildcard>
                        <area>0</area>
                     </network>
                        
                     <network>
                        <ip>10.10.23.0</ip>
                        <wildcard>0.0.0.3</wildcard>
                        <area>0</area>
                     </network>
        </process-id>
     </ospf>
   </router-ospf>
  </router>
 </native>
</config>"""
