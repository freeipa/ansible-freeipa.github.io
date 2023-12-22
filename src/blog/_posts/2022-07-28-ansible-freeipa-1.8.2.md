---
layout: post
title: "ansible-freeipa-1.8.2"
section: Blog
date: 2022-07-28T14:38:00
author: Thomas Woerner
category: release
tags:
  - release
---

Highlights in version 1.8.2
-------------------
  - SIDs are always generated for server and replica deployments
  - Random Serial Numbers are not enabled by default any more
  - Fixes comparison of bool values in IPA 4.9.10+ for ipadnsconfig
  - Fixes issue with using an IP address for the server in client deployments

Changes since 1.8.1
-------------------

  - ipaclient: Removed invalid call `logger.info()` (#867)
  - ipaserver/ipareplica: Always generate SIDs (#866)
  - ipaserver,ipareplica: Fix Random Serial Numbers always enabled (#864)
  - ipadnsconfig: Fix boolean values comparison (#863)
  - ansible_freeipa_module: Use ipaplatform.tasks.parse_ipa_version (#859)
  - upstream CI: enable tests on Fedora Rawide. (#854)
  - sanity.sh: Allow use of podman instead of docker (#850)

Detailed changelog since 1.8.1 by author
----------------------------------------
  3 authors, 10 commits

Rafael Guterres Jeffman (6)

  - ipadnsconfig: Disable only tests that are failing due to python-dns
  - ipadnsconfig: Separate tests for forwarders with custom ports.
  - ipadnsconfig: Enable chech_mode support
  - ipadnsconfig: Fixe comparison of bool values in IPA 4.9.10+
  - sanity.sh: Allow use of podman instead of docker
  - upstream CI: enable tests on Fedora Rawide.

Thomas Woerner (3)

  - ipaserver/ipareplica: Always generate SIDs
  - ipaserver,ipareplica: Fix Random Serial Numbers always enabled
  - ansible_freeipa_module: Use ipaplatform.tasks.parse_ipa_version

jpclipffel (1)

  - ipaclient: Removed invalid call `logger.info()`

Information at GitHub
---------------------
* Release: [1.8.2](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.8.2)
* Tarball: [ansible-freeipa-1.8.2.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.8.2.tar.gz)
