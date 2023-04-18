---
layout: post
title: "ansible-freeipa-1.5.0"
section: Blog
date: 2021-12-02T13:48:00
author: Thomas Woerner
category: release
---

Highlights in version 1.5.0
-------------------

  - Automation Hub demands that the version of an Ansible Collection is at minumum 1.0.0, therefore the major version of ansible-freeipa has been increased by 1.
  - Several changes to be able to pass Automation Hub tests.
  - Idempotency fixes in ipaautomember, ipaservice and ipasudorule.
  - Upstream tests against multiple Ansible versions.

Changes since 0.4.2
-------------------

  - build-galaxy-release: Cleanup of ipabackup_get_backup_dir.py link (#692)
  - Changes needed to pass Automation Hub tests (#691)
  - CI: Add supoprt for Shellcheck (#690)
  - ansible_module_utils: Add method to get parameters as lowercase. (#683)
  - automember: Fix behavior of unused parameters. (#675)
  - ipaprivilege: Fix permissions handling. (#670)
  - ipaservice: Use IPAAnsibleModule member result handler. (#668)
  - ipaservice: Fix idempotent behavior for principal aliases. (#667)
  - sudorule: Fix runas with external users and groups. (#665)
  - CI: Test modules against Ansible core 2.11 and latest Ansible (#612)

Detailed changelog since 0.4.2 by author
----------------------------------------
  2 authors, 23 commits

Rafael Guterres Jeffman (12)

  - ipaservice: Remove custom error handler.
  - ipaservice: Use gen_*_lists to avoid unneded API calls.
  - linters: Fix shellcheck warnings in 'utils' scripts.
  - shellcheck: Run shellcheck as a Github action.
  - pre-commit: Add shellcheck to pre-commit configuration.
  - CI: Test modules against different Ansible versions.
  - ansible_module_utils: Add method to get parameters as lowercase.
  - automember: Fix behavior of unused parameters.
  - sudorule: Fix runas with external users and groups.
  - ipaprivilege: Fix module execution in check_mode.
  - ipaprivilege: fix creation of add/del lists for permissions.
  - ipaservice: Fix idempotent behavior for principal aliases.

Thomas Woerner (11)

  - build-galaxy-release: Cleanup of ipabackup_get_backup_dir.py link
  - pylint upstream: Ignore __metaclass__
  - yamllint: Fix EXAMPLE issues
  - shellcheck: Double quote to prevent globbing and word splitting
  - Use `ansible.module_utils.six` instead of `six`
  - Add missing whitespace around arithmetic operator
  - ipaclient_get_facts: Fix closing bracket does not match indentation
  - Remove "’" from yaml files
  - Replace asserts with raise AssertionError
  - Remove non-module shebang
  - Add __future__ imports and __metaclass__ for automationhub

Information at GitHub
---------------------
* Release: [1.5.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.5.0)
* Tarball: [ansible-freeipa-1.5.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.5.0.tar.gz)
