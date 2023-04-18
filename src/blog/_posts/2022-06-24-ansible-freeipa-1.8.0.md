---
layout: post
title: "ansible-freeipa-1.8.0"
section: Blog
date: 2022-06-24T14:19:00
author: Thomas Woerner
category: release
---

Highlights in version 1.8.0
-------------------

  - New roles for smartcard server and client setup
  - idrange module fixes
  - Upstream CI enhancements

Changes since 1.7.0
-------------------

  - upstream CI: Update nightly Ansible versions. (#844)
  - utils/changelog: Fixed --tag option, new --galaxy option (#842)
  - requirements-dev: Update requirements for virtual environments (#841)
  - New roles for smartcard server and client setup (#838)
  - idrange: Fix typo in test comments. (#833)
  - idrange: Fix list of invalid parameters for 'state:absent'. (#832)
  - idrange: Fix usage of dom_name when idrange doesn't exist. (#831)
  - Fix ansible-test sanity missing CHANGELOG.rst. (#830)
  - utils/build-galaxy-release.sh: Add "-i" to install generated collection (#829)
  - Upstream CI updates. (#827)
  - upstream CI: Add support for testing ansible-freeipa as a collection. (#825)
  - Add support to define which playbook tests to execute with pytest. (#354)

Detailed changelog since 1.7.0 by author
----------------------------------------
  2 authors, 21 commits

Rafael Guterres Jeffman (18)

  - upstream CI: Enable tests using ansible-core 2.12.
  - upstream CI: Remove Ansible 2.9 from test matrix
  - idrange: Fix list of invalid parameters for 'state:absent'.
  - upstream CI: Add support for testing ansible-freeipa as a collection.
  - pylint: Ignore module ipaserver.dcerpc errors.
  - idrange: Fix addition of idrange with dom_name.
  - ansible_module_utils: add method to retrive SID from dom_name.
  - requirements-dev: Update requirements for virtual environments
  - fixup! Add support to define which playbook tests to execute with pytest.
  - upstream tests: Disable dnsconfig and dnsforwardzone
  - tests/utils.py: Fix pylint issues.
  - Add support to define which playbook tests to execute with pytest.
  - build-galaxy-release: Automatically create CHANGELOG.
  - idrange: Fix typo in test comments.
  - upstream CI: Update default ansible-core version to 2.12.
  - upstream CI: Allow the use of latest ansible-core.
  - upstream CI: removed all CentOS 8 support.
  - upstream CI: Relabel upstream PR pipeline jobs.

Thomas Woerner (3)

  - New roles for smartcard server and client setup
  - utils/changelog: Fixed --tag option, new --galaxy option
  - utils/build-galaxy-release.sh: Add "-i" to install generated collection

Information at GitHub
---------------------
* Release: [1.8.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.8.0)
* Tarball: [ansible-freeipa-1.8.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.8.0.tar.gz)
