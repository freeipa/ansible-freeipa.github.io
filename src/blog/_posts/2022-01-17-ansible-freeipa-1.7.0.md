---
layout: post
title: "ansible-freeipa-1.6.0"
section: Blog
date: 2022-01-17T09:39:00
author: Thomas Woerner
category: release
---

Highlights in version 1.6.0
-------------------
  - New managament modules for automount keys and maps. Indirect automount maps are not supported yet.
  - The sudorule and role management modules are now creating FQDN lowercase from all hostnames to fix idempotency issues with single names, mixed case names and FQDN.
  - The idempotency issues with members in role, hbacsvcgroup and hbacrule management modules have been fixed. The modules are now comparing members lowercase.
  - The role management module is now supporting the state `renamed` for role renaming in the same way as other modules do.
  - The group management module is now properly handling lists of members, where some are already part or not part of the group.
  - The build-galaxy-release.sh script has been extended and fixed. It is now using a build directory and is not resetting uncommitted changes anymore.
  - ansible-test is now also used in the upstream tests.
  - Several fixes to pre-commit, upstream tests and workflows.

Changes since 1.5.3
-------------------

  - ansible-test: Fix new findings (#729)
  - pre-commit: Update ansible-lint version to v5.3.2 (#728)
  - pre-commit: Use system shellcheck. (#727)
  - Github Workflows: Run ansible-lint without an action. (#726)
  - ansible-test fixes (#725)
  - build-galaxy-release.sh: Use build dir, new options, checks, no reset (#724)
  - Enable ansible-test in github workflow (#723)
  - ipagroup: Refactor and fix group member management. (#721)
  - upstream CI: Wait for KDC to be available. (#717)
  - iparole: Add state 'renamed'. (#716)
  - Enable pylint for ansible-freeipa roles. (#708)
  - upstream CI: Enable nightly tests using ansible-core 2.12. (#706)
  - upstream CI: Enable ansible-doc-test for ansible-core 2.12. (#704)
  - upstrem CI: Fix Ansible version in pytest playbooks. (#697)
  - upstream CI:  Add support for CentOS 9 stream. (#696)
  - hbacrule: Fix member management idempotence issues. (#686)
  - hbacsvcgroup: Fix member management idempotence issues. (#685)
  - iparole: Fix idempotence issues (#684)
  - sudorule: Create FQDN from single hostnames (#674)
  - add module to create and manage automount keys (#498)
  - add module to create and manage automount maps (#497)

Detailed changelog since 1.5.3 by author
----------------------------------------
  3 authors, 34 commits

Rafael Guterres Jeffman (27)

  - iparole: Skip ansible-test verifications for Python 2.6.
  - hbacrule: Fix member management idempotence issues.
  - test playbooks: Add fact to define ipaserver_domain if not set.
  - pre-commit: Use system shellcheck.
  - Github Workflows: Run ansible-lint without an action.
  - iparole: Add tests to verify if capitalisation is ignored.
  - iparole: rename function get_lowercase to result_get_value_lowercase
  - iparole: Fix idempotence issues with members.
  - iparole: Ensure host members are lowercase and FQDN.
  - IPAAnsibleModule: cache IPA domain.
  - iparole: Case insensitive comparison of service members.
  - iparole: Remove custom code in favor of commom functions.
  - iparole: Removed unused code.
  - pylint: Enable pylint for ansible-freeipa roles.
  - pylint: Fix pylint issues with modules.
  - pylint: Add modules and names that should be ignored by linter.
  - Fixed automountkey code review issues.
  - Adapt automount to IPAAnsibleModule and add code review modifications.
  - ipagroup: Refactor and fix group member management.
  - upstream CI: Wait for KDC to be available.
  - iparole: Add state 'renamed'.
  - sudorule: Create FQDN from single hostnames
  - upstream CI: Enable ansible-doc-test for ansible-core 2.12.
  - upstream CI: Enable nightly tests using ansible-core 2.12.
  - hbacsvcgroup: Fix member management idempotence issues.
  - ci: Add support for CentOS 9 Stream on upstream CI.
  - upstrem CI: Fix Ansible version in pytest playbooks.

Thomas Woerner (5)

  - ansible-test: Fix new findings
  - pre-commit: Update ansible-lint version to v5.3.2
  - ansible-test fixes
  - Enable ansible-test in github workflow
  - build-galaxy-release.sh: Use build dir, new options, checks, no reset

chrisp (2)

  - New automount key management module
  - New automount map management module.

Information at GitHub
---------------------
* Release: [1.6.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.6.0)
* Tarball: [ansible-freeipa-1.6.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.6.0.tar.gz)
