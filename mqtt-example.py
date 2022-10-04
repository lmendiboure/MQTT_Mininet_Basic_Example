"""Custom topology example for MQTT implementation

In this architecture we simply consider three switches and three hosts : h3 is the broker and h1 and h2 are simple subscribers.

Note that: the automatic generation of periodic messages could simply be added to this script (Sleep + cmd("python mosquitto-pub.py")
"""
import os
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        
        # Used as Broker in this simple example
        
        centralHost = self.addHost( 'h3' )
        
        
        leftSwitch = self.addSwitch( 's1' )
        centralSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, centralSwitch )
        self.addLink( centralSwitch, centralHost )
        self.addLink( centralSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    os.system('mn -c')
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    
    
    #launch mosquitto broker on h3
    liste=['h3']
    for el in liste:
    	node = net.get(el)
    	node.cmd('mosquitto -v -p 1883:1883 -c /etc/mosquitto/mosquitto.conf &')
    	
    #launch mosquitto_sub on h1 and h3
    
    liste=['h1','h3']
    i=1 #variable used to indicate subscriber number
    for el in liste:
    	node = net.get(el)
    	cmd="python mosquitto-sub.py "+str(i)+ " &"
    	node.cmd(cmd)
    	i+=1
    
    CLI(net)
    net.stop()
    
    
