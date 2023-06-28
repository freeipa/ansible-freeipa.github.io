---
layout: post
title: "ansible-freeipa-1.6.2"
section: Blog
date: 2022-01-26T15:22:00
author: Thomas Woerner
category: release
tags:
  - release
---

Changes since 1.6.1
-------------------

  - ipauser: Fix idempotence issue when using 'preserved'. (#749)
  - dnsconfig: Add 'action: member' to dnsconfig example playbooks. (#748)
  - sudorule: Fix management of deny_sudocmdgroup. (#744)
  - group: Services are ipapython.kerberos.Principal and case insensitive (#742)

Detailed changelog since 1.6.1 by author
----------------------------------------
  2 authors, 5 commits

Rafael Guterres Jeffman (4)

  - ipauser: Make 'no user' messages consistent.
  - ipauser: Fix idempotence issue when using 'preserved'.
  - dnsconfig: Add 'action: member' to dnsconfig example playbooks.
  - sudorule: Fix management of deny_sudocmdgroup.

Thomas Woerner (1)

  - group: Services are ipapython.kerberos.Principal and case insensitive

Information at GitHub
---------------------
* Release: [1.6.2](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.6.2)
* Tarball: [ansible-freeipa-1.6.2.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.6.2.tar.gz)
