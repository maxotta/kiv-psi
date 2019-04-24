# SNMP demo

Simple SNMP (Simple Network Management protocol) demo

## How to run this demo

This demo requires [VirtualBox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/) and [Ansible](https://www.ansible.com/) to be working on your machine. With the help of *Vagrant* you bring up two VMs, both running Linux *CentOS* with *SNMP daemons* up and running:
```
    cd snmp
    vagrant up
```
Example output:
```
...
==> node-1: Machine 'node-1' has a post `vagrant up` message. This is a message
==> node-1: from the creator of the Vagrantfile, and not from Vagrant itself:
==> node-1:
==> node-1: SNMP stuff ready.

==> node-2: Machine 'node-2' has a post `vagrant up` message. This is a message
==> node-2: from the creator of the Vagrantfile, and not from Vagrant itself:
==> node-2:
==> node-2: SNMP stuff ready.
```

After that you can 'ssh' to one of the nodes and use the *snmpwalk* utility to retrieve a subtree of management values using SNMP GETNEXT requests depending on the *community* identifier provided:
```
    vagrant ssh node-1
    ...
    snmpwalk -v 2c -c psi-config -O e node-2.local
    ...
    snmpwalk -v 2c -c psi-all -O e node-2.local
    ...
```
When you're finished, you can stop the VM by issuing the command:
```
    vagrant halt
```
or to get completely rid of the VMs by entering:
```
    vagrant destroy
```

