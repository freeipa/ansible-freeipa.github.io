---
layout: page
title: Requirements
---

## Supported FreeIPA Versions ##

FreeIPA versions 4.6 and up are supported by all roles.

The client role supports versions 4.4 and up, the server role is working with versions 4.5 and up, the replica role is currently only working with versions 4.6 and up.

## Supported Distributions ##

* RHEL/CentOS 7.4+
* Fedora 26+
* Ubuntu
* Debian 10+ (ipaclient only, no server or replica!)

## Requirements ##

### Controller ###

* Ansible version: 2.8+ (ansible-freeipa is an Ansible Collection)
* /usr/bin/kinit is required on the controller if a one time password (OTP) is used

### Node ###

* Supported FreeIPA version (see above)
* Supported distribution (needed for package installation only, see above)

## Limitations ##

**External signed CA**

External signed CA is now supported. But the currently needed two step process is an issue for the processing in a simple playbook.

Work is planned to have a new method to handle CSR for external signed CAs in a separate step before starting the server installation.
