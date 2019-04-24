# Ansible Roles Library

Contains Ansible roles for use in Vagrant provisioning.
Currently implemented roles:
* **common** - adds EPEL repo, Midnight Commander and Screen utilities
* **development** - installs packages from the *Development Tools* group (gcc, make, etc.)
* **java** - installs current JDK
* **multicast-dns** - sets up AVAHI mDNS, so we can access VM nodes over DNS names like *node-1.local*
* **python** - installs Python 3 and other related stuff (pip, development headers, etc)
* **snmp** - installs and sets up SNMP daemon and utilities

  