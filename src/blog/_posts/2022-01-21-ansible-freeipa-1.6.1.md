---
layout: post
title: "ansible-freeipa-1.6.1"
section: Blog
date: 2022-01-21T16:39:00
author: Thomas Woerner
category: release
tags:
  - release
---

Highlights in version 1.6.1
-------------------

  - No gssapi use in ipaclient_get_keytab. The requirement for gssapi on the controller is therefore not needed anymore for OTP with keytab.
  - Idempotency fixes in sudorule, dnsconfig and hostgroup management modules.
  - Member support for forwarders in dnsconfig management module.

Changes since 1.6.0
-------------------

  - automountmap: Add client context test playbook. (#741)
  - User tests: Extend expiration dates for client on server test (#739)
  - sudorule: fix idempotence issues and refactor. (#738)
  - dnsconfig: add support for 'action: member'. (#737)
  - ipahostgroup: Ensure host members are lowercase and FQDN (#736)
  - dnsconfig: Fix management of forwarders. (#735)
  - README test: Also check role readme files (#734)
  - ipaclient_get_keytab: Do not use gssapi for kinit_keytab (#733)
  - README.md: Add automount key and map, fix ref to hbacsvcgroup and test (#731)

Detailed changelog since 1.6.0 by author
----------------------------------------
  2 authors, 9 commits

Rafael Guterres Jeffman (4)

  - automountmap: Add client context test playbook.
  - dnsconfig: add support for 'action: member'.
  - sudorule: fix idempotence issues and refactor.
  - dnsconfig: Fix management of forwarders.

Thomas Woerner (5)

  - User tests: Extend expiration dates for client on server test
  - ipahostgroup: Ensure host members are lowercase and FQDN
  - README test: Also check role readme files
  - ipaclient_get_keytab: Do not use gssapi for kinit_keytab
  - README.md: Add automount key and map, fix ref to hbacsvcgroup and test

Information at GitHub
---------------------
* Release: [1.6.1](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.6.1)
* Tarball: [ansible-freeipa-1.6.1.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.6.1.tar.gz)
