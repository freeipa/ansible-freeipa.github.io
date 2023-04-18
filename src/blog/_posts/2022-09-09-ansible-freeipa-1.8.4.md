---
layout: post
title: "ansible-freeipa-1.8.4"
section: Blog
date: 2022-09-09T08:05:00
author: Thomas Woerner
category: release
---

Highlights in 1.8.4
-------------------
 - Support for SID related attributes in ipaconfig
 - Minimum value check of idstart parameter for ipaserver role
 - Deployment roles fixes and optimization
 
Changes since 1.8.3
-------------------

  - ipaconfig: Fix example playbook titles. (#912)
  - utils/ansible-freeipa.spec.in: Sync with Fedora rawhide spec file (#911)
  - upstream CI: Force retrieval of ansible-freeipa master. (#910)
  - upstream CI: Ensure 'master' branch is available for set_test_modules (#908)
  - ipaconfig: Add support for SID related attributes. (#906)
  - ipaserver/ipareplica: Add isatty method to AnsibleModuleLog (#905)
  - ipabackup: Fix order of ipabackup_name parameter evaluation. (#904)
  - ipabackup: Add playbook tests for ipabackup. (#901)
  - ipaserver: Add missing idstart check (#897)
  - fedora rawhide: Temporarily disable failing DNS tests (#895)
  - ipaserver: ipaclient part does not need to install packages (#894)
  - upstream CI: run PR tests only for affected plugins (#893)
  - Fix short_description flag in plugins, role modules and templates (#892)
  - upstream CI: Fix list evaluation in IPA_ENABLED/IPA_DISABLED tests (#890)
  - ipauser: Add note on attributes 'first' and 'last' requirements (#889)
  - ipasudorule: Fix usage of 'action' and 'state' in examples. (#887)
  - upstream CI: enable/disable tests based on test image (#884)
  - ipareplica: Do not overwrite ipaclient_no_ntp for client part deployment (#876)
  - Run tests locally with upstream CI images. (#849)

Detailed changelog since 1.8.3 by author
----------------------------------------
  2 authors, 24 commits

Rafael Guterres Jeffman (17)

  - ipaconfig: Add support for SID related attributes.
  - ipaconfig: Fix example playbook titles.
  - upstream CI: Force retrieval of ansible-freeipa master.
  - upstream CI: Force retrieval of ansible-freeipa master.
  - ipabackup: Fix order of ipabackup_name parameter evaluation.
  - upstream CI: Ensure 'master' branch is available for set_test_modules
  - ipabackup: Add playbook tests for ipabackup.
  - upstream CI: run PR tests only for affected plugins
  - check_test_configuration: Add support for IPA_* environment variables
  - tests: Drop pytest-split-tests in favor of pytest-split
  - run-tests: Run tests locally with upstream CI images
  - upstream CI: Fix list evaluation in IPA_ENABLED/IPA_DISABLED tests
  - ipauser: Add note on attributes 'first' and 'last' requirements
  - upstream ci: Add step to display scenario configuration
  - upstream ci: Avoid scheduling tests that will not be executed.
  - upstream ci: Add support for distro specific test configuration.
  - ipasudorule: Fix usage of 'action' and 'state' in examples.

Thomas Woerner (7)

  - utils/ansible-freeipa.spec.in: Sync with Fedora rawhide spec file
  - ipaserver/ipareplica: Add isatty method to AnsibleModuleLog
  - ipaserver: Add missing idstart check
  - fedora rawhide: Temporarily disable failing DNS tests
  - ipaserver: ipaclient part does not need to install packages
  - Fix short_description flag in plugins, role modules and templates
  - ipareplica: Do not overwrite ipaclient_no_ntp for client part deployment

Information at GitHub
---------------------
* Release: [1.8.4](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.8.4)
* Tarball: [ansible-freeipa-1.8.4.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.8.4.tar.gz)
