---
layout: post
title: "ansible-freeipa-1.7.0"
section: Blog
date: 2022-04-29T15:16:00
author: Thomas Woerner
category: release
---

Highlights in version 1.7.0
-------------------

  - New idrange management module.
  - New servicedelegationrule management module.
  - New servicedelegationtarget management module.
  - Add support for managing idoverrideusers in ipagroup.
  - hbacrule: Allow clearing members with empty lists.
  - Fail on empty strings for list parameters with choices that do not contain empty strings.

Changes since 1.6.3
-------------------

  - ipaautomountmap: Fix parameter evaluation. (#820)
  - ansible-lint: Identify env_*.yml and tasks_*.yml as task files. (#818)
  - New idrange management module (#813)
  - ipatrust: fix range_type and test enhancement. (#810)
  - ipatrust: Set valid choices for trust_type. (#808)
  - DNS forward policy: ensure consistency between module parameters. (#807)
  - utils/new_module templates: Add missing password to example playbooks. (#805)
  - Update README-group.md (#799)
  - Ensure example playbooks have ipaadmin_password and it is the standard one. (#793)
  - Update pylint to version 2.12.2 (#791)
  - automember: Remove debug output (#783)
  - module_utils: Fix comparison of elements not in IPA object. (#780)
  - module_params_get*: Fail on empty string in string list parameters (#779)
  - upstream ci: Fix scenario for Centos 8 Stream with Ansible 2.11. (#777)
  - ansible-lint: Remove warning on 'ignore_errors'. (#776)
  - upstream CI: Fix container builds in face of Ansible and CentOS changes. (#775)
  - molecule: Disable prerun for normal tests (#774)
  - servicedelegation: Do not fail for not existing members with state absent (#773)
  - Fix new ansible-lint findings (#772)
  - build-galaxy-release: Fix refs for all doc_fragments in plugins/doc_fragments (#771)
  - upstream ci: Rename CentOS 9 pipelines jobs to c9s. (#770)
  - test_servicedelegationtarget.yml: Added list tests (#769)
  - New servicedelegationrule management module (#766)
  - IPAAnsibleModule: Provide base configuration for delete_continue. (#761)
  - upstream ci: enable ansible-core 2.12 for CentOS 9 Stream. (#758)
  - Update module templates to current practices. (#757)
  - New servicedelegationtarget management module (#756)
  - Fixes `no_log` warning for `ipahost` module (#755)
  - hbacrule: Allow clearing members with empty lists. (#752)
  - upstream CI: Enable CentOS 8 Stream for PR and nightly tests. (#732)
  - Add support for managing idoverrideusers in ipagroup. (#487)

Detailed changelog since 1.6.3 by author
----------------------------------------
  4 authors, 55 commits

Austin (1)

  - Fixes `no_log` warning for `ipahost` module

Rafael Guterres Jeffman (35)

  - New idrange management module
  - ipaautomountmap: Fix error messages for invalid 'name' sizes.
  - ipaautomountmap: Force setting automountmapname in IPA API calls.
  - Add support for managing idoverrideusers in ipagroup.
  - ipatrust: Fix support for `range_type`.
  - tests/trust: Improved test coverage and execution.
  - tests/ipatrust: Modify AD realm name to an invalid name.
  - ipatrust: Updated ipatrust documentation.
  - ipatrust: Set valid choices for trust_type.
  - ipaautomountmap: Allows clearing description attribute with "".
  - ipauser: Refactor module due to fix on arguments comparison.
  - module_utils: Fix comparison of elements not in IPA object.
  - ansible-lint: Identify env_*.yml and tasks_*.yml as task files.
  - DNS forward policy: ensure consistency between module parameters.
  - utils/new_module templates: Add missing password to example playbooks.
  - example playbooks: ipaadmin_password is used and consistent.
  - Removed vim swap file from the repository.
  - pylint: Bump version to 2.12.2.
  - pylint: Ignore global-variable-not-assigned
  - pylint: Ignore consider-using-f-string.
  - module templates: Add delete_commit code template.
  - module templates: Add example and note for case insensitive members.
  - module templates: Refactor member management.
  - IPAAnsibleModule: Provide base configuration for delete_continue.
  - upstream ci: Fix scenario for Centos 8 Stream with Ansible 2.11.
  - upstream ci: Rename CentOS 9 pipelines jobs to c9s.
  - ansible-lint: Remove warning on 'ignore_errors'.
  - upstream CI: Use fedora-latest as default test container.
  - upstream CI: Update Python version when building containers.
  - upstream CI: Enable CentOS 8 Stream for PR and nightly tests.
  - ci images: Fix creation of CentOS 9 stream test container.
  - molecule: Disable prerun for build containers.
  - build containers: Allow setting of Python version used.
  - hbacrule: Allow clearing members with empty lists.
  - upstream ci: enable ansible-core 2.12 for CentOS 9 Stream.

Thomas Woerner (18)

  - automember: Remove debug output
  - ipaconfig: Set allow_empty_string for user_auth_type, pac_type, configstring
  - ipahost: Set allow_empty_string for auth_ind
  - ipaservice: Set allow_empty_string for auth_ind and pac_type
  - ipauser: Set allow_empty_string for userauthtype and sshpubkey
  - module_params_get*: Fail on empty string in string list parameters
  - molecule: Disable prerun for normal tests
  - servicedelegation: Do not fail for not existing members with state absent
  - tests/vault/test_vault_change_type.yml: Use lower case var names
  - tests/role/test_role_lists_handling.yml: Use lower case var names
  - tests/env_freeipa_facts.yml: Use lower case var names
  - tests/config/test_config.yml: Use named tasks
  - ipaclient install.yml: Use named tasks
  - build-galaxy-release: Fix refs for all doc_fragments in plugins/doc_fragments
  - test_servicedelegationtarget.yml: Added list tests
  - New servicedelegationrule management module
  - New servicedelegationtarget management module
  - ansible_freeipa_module: New function servicedelegation_normalize_principals

vjs2174 (1)

  - Update README-group.md

Information at GitHub
---------------------
* Release: [1.7.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.7.0)
* Tarball: [ansible-freeipa-1.7.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.7.0.tar.gz)
