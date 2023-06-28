---
layout: post
title: "ansible-freeipa-1.9.1"
section: Blog
date: 2023-01-30T03:54:00
author: Thomas Woerner
category: release
tags:
  - release
---

Highlights in 1.9.1
-------------------

- Ansible 2.14 test and lint fixes
- pwpolicy: Allow clearing policy values
- More bug fixes

Changes since 1.9.0
-------------------

  - upstream CI: increase Azure test timeout. (#1031)
  - Use yml extension for pytest tests (#1030)
  - playbooks: Fix automount tasks to make ansible-lint happy (#1029)
  - dnszone tests: Fix typo on task names. (#1028)
  - playbooks/automount: All playbooks should use .yml (#1027)
  - Ansible lint tests (#1026)
  - pwpolicy: Fix tests for 'minlength: ""' (#1024)
  - .github/workflows/lint.yml: ansible-lint needs collection source dir (#1023)
  - pwpolicy: Fix new bool checks for IPA prior to 4.9.10 (#1022)
  - utils files: Support builtins with ansible.builtin. prefix (#1016)
  - Fix ansible-test lint warnings in roles. (#1014)
  - yamllint: All tasks need to be named (#1013)
  - pwpolicy: Allow clearing policy values. (#1012)
  - upstream ci: Allow tasks to retry in case of connection failure. (#1009)
  - Use FQCN for ansible.builtin (#1007)
  - Use netgroup_find instead of netgroup_show to workaround IPA bug. (#1003)
  - ansible-freeipa.spec.in: Fix for loop with wildcard (#1002)
  - Update development and Github workflow tools. (#999)
  - upstream ci: Update Ansible versions on Azure pipelines. (#977)

Detailed changelog since 1.9.0 by author
----------------------------------------
  3 authors, 66 commits

Denis Karpelevich (1)

  - Use netgroup_find instead of netgroup_show to workaround IPA bug.

Rafael Guterres Jeffman (19)

  - upstream CI: increase Azure test timeout.
  - playbooks: Fix automount tasks to make ansible-lint happy
  - dnszone tests: Fix typo on task names.
  - pwpolicy: Fix tests for 'minlength: ""'
  - ansible-lint: Fix file kind and ignores.
  - roles: Fix ansible-lint name:template warnings
  - roles: Fix ansible-lint warning on var-naming.
  - Fix issues raised by Flake8 version 5.0.3
  - Fix issues raised by Pylint version 2.14.4.
  - Update Github workflow linter and check tools.
  - pwpolicy: Allow clearing policy values.
  - upstream ci: Update Ansible versions on Azure pipelines.
  - Update development tools.
  - roles: Fix when, block and always key order.
  - roles: Fix jinja2 template spacing
  - roles: Fix task names to start with uppercase letters
  - roles: Fix use of ansible.builtin.fail free-form message.
  - roles: Fix type of data used for for versions in meta files
  - upstream ci: Allow tasks to retry in case of connection failure.

Thomas Woerner (46)

  - Use yml extension for pytest tests
  - playbooks/automount: All playbooks should use .yml
  - ansible-lint: All names should start with an uppercase letter
  - Fix jinja2 white spaces issues reported by ansible-lint
  - Improve jinja2 spacing: Remove space between join and ()
  - .github/workflows/lint.yml: Enable ansible-lint for the whole collection
  - .ansible-lint: Deactivate experimental and name[template] tests
  - .github/workflows/lint.yml: ansible-lint needs collection source dir
  - pwpolicy: Fix new bool checks for IPA prior to 4.9.10
  - yamllint: All tasks need to be named
  - utils/get_test_modules.py: Support ansible.builtin. prefix
  - utils/galaxyfy.py: Support builtins with ansible.builtin. prefix
  - vault: Use FQCN for ansible.builtin
  - user: Use FQCN for ansible.builtin
  - trust: Use FQCN for ansible.builtin
  - sudo*: Use FQCN for ansible.builtin
  - servicedelegation*: Use FQCN for ansible.builtin
  - service: Use FQCN for ansible.builtin
  - server: Use FQCN for ansible.builtin
  - selfservice: Use FQCN for ansible.builtin
  - role: Use FQCN for ansible.builtin
  - pwpolicy: Use FQCN for ansible.builtin
  - privilege: Use FQCN for ansible.builtin
  - permission: Use FQCN for ansible.builtin
  - netgroup: Use FQCN for ansible.builtin
  - location: Use FQCN for ansible.builtin
  - idrange: Use FQCN for ansible.builtin
  - host*: Use FQCN for ansible.builtin
  - hbac*: Use FQCN for ansible.builtin
  - group: Use FQCN for ansible.builtin
  - tests/external-signed-ca-*: Use FQCN for ansible.builtin
  - tests/env_freeipa_facts.yml: Use FQCN for ansible.builtin
  - dnszone: Use FQCN for ansible.builtin
  - dnsrecord: Use FQCN for ansible.builtin
  - dnsforwardzone: Use FQCN for ansible.builtin
  - dnsconfig: Use FQCN for ansible.builtin
  - delegation: Use FQCN for ansible.builtin
  - config: Use FQCN for ansible.builtin
  - tests/ca-less: Use FQCN for ansible.builtin
  - automount: Use FQCN for ansible.builtin
  - automember: Use FQCN for ansible.builtin
  - ipabackup role: Use FQCN for ansible.builtin
  - ipaclient role: Use FQCN for ansible.builtin
  - ipareplica role: Use FQCN for ansible.builtin
  - ipaserver role: Use FQCN for ansible.builtin
  - ansible-freeipa.spec.in: Fix for loop with wildcard

Information at GitHub
---------------------
* Release: [1.9.1](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.9.1)
* Tarball: [ansible-freeipa-1.9.1.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.9.1.tar.gz)
