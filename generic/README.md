# Generic Vagrant Project

Use this project as a workbench for the practical classes.

You can easily create a cluster of several identical CentOS 8 Linux boxes with "Development Tools" installed (gcc, make, etc.). The sources of provided examples are available inside each box at ```/shared-folder/src```

By default, the ```vagrant up``` command will create one node, if you want to create more nodes, you have to set the environment variable ```CLUSTER_NODES``` to the desired number of nodes. For example the commands

```
export CLUSTER_NODES=3
vagrant up
```
will create and startup 3 nodes named ```node-1```, ```node-2``` and ```node-3``` with ip addresses ```10.0.1.101```, ```10.0.1.102``` and ```10.0.1.103```.

You can connect to a node with the ```vagrant ssh node-1``` command.

⚠️ **IMPORTANT NOTE:** Even if you run 'just' ```vagrant ssh```, but **in a different terminal**, the variable ```CLUSTER_NODES``` **must be set** and have the same value! ⚠️
