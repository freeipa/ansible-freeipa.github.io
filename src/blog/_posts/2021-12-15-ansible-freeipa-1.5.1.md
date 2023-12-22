---
layout: post
title: "ansible-freeipa-1.5.1"
section: Blog
date: 2021-12-15T09:02:00
author: Thomas Woerner
category: release
tags:
  - release
---

Highlights in version 1.5.1
-------------------

  - More changes related to Automation Hub tests.
  - Deprecation of FreeIPABaseModule in favor of IPAAnsibleModule.
  - Ubuntu 18.04 deployment fixes.
  - Documentation fixes.

Changes since 1.5.0
-------------------

  - More Automation Hub fixes (#709)
  - yamllint: Fix missing document start. (#705)
  - correct comment in example playbook (#703)
  - Login shell is called defaultshell and not defaultlogin (#702)
  - Fix role issues in Debian based distros. (#699)
  - upstream ci: Build images for CentOS 9 Stream. (#698)
  - Deprecate FreeIPABaseModule in favor of IPAAnsibleModule. (#671)

Detailed changelog since 1.5.0 by author
----------------------------------------
  3 authors, 15 commits

Rafael Guterres Jeffman (7)

  - yamllint: Fix missing document start.
  - upstream ci: Build images for CentOS 9 Stream.
  - Debian Buster: Fix "No module named 'ipapython'".
  - Ubuntu 18.04: Fix role instalation for Ubuntu Bionic Beaver.
  - DNSZone: Use IPAAnsibleModule.
  - automountlocation: Use IPAAnsibleModule.
  - Deprecate FreeIPABaseModule in favor of IPAAnsibleModule.

Thomas Woerner (6)

  - Fix ansible-test reported pep8 errors
  - ipabackup_get_backup_dir.py: Add missing ":" in example
  - Ignore file for ansible-test sanity 2.12
  - utils/gen_module_docs.py: Drop duplicate setup_adtrust key
  - Add version for ansible deprecated calls
  - build-galaxy-release: Real cleanup of ipabackup_get_backup_dir.py link

jh23453 (2)

  - correct comment in example playbook
  - Login shell is called defaultshell and not defaultlogin

Information at GitHub
---------------------
* Release: [1.5.1](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.5.1)
* Tarball: [ansible-freeipa-1.5.1.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.5.1.tar.gz)
