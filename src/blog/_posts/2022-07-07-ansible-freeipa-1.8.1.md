---
layout: post
title: "ansible-freeipa-1.8.1"
section: Blog
date: 2022-07-07T10:57:00
author: Thomas Woerner
category: release
---

Highlights in version 1.8.1
-------------------

  - Support for FreeIPA 4.9.10
  - Support for ansible 2.13
  - Support for Python 3.11

Changes since 1.8.0
-------------------

  - tests/server/test_server.yml: Fix generation of ipaserver_domain (#857)
  - Provide own getargspec for roles and modules with Python 3.11 (#856)
  - ipaserver: Use jinja for list concatenation (#853)
  - ipaserver,ipareplica: Add random_serial_numbers to options (#852)
  - Fix handling of boolean values for FreeIPA 4.9.10+ (#851)

Detailed changelog since 1.8.0 by author
----------------------------------------
  2 authors, 8 commits

Rafael Guterres Jeffman (4)

  - pytests/test_dnszone: Fix evaluation of boolean values
  - pytest tests: Enhanced assertion for check_* methods.
  - api_check_ipa_version: Fix version comparison for more than one digit
  - Fix handling of boolean values for FreeIPA 4.9.10+

Thomas Woerner (4)

  - tests/server/test_server.yml: Fix generation of ipaserver_domain
  - Provide own getargspec for roles and modules with Python 3.11
  - ipaserver,ipareplica: Add random_serial_numbers to options
  - ipaserver: Use jinja for list concatenation

Information at GitHub
---------------------
* Release: [1.8.1](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.8.1)
* Tarball: [ansible-freeipa-1.8.1.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.8.1.tar.gz)
