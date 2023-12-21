---
layout: post
title: "ansible-freeipa-1.11.1"
section: Blog
date: 2023-07-24T13:05:00
author: Thomas Woerner
category: release
---

Highlights in 1.11.1
--------------------

- Support for GECOS, street, smb and idp attributes in ipauser module
- Support for indirect maps in ipaautomountmap module
- Update of user_auth_type choices in ipaconfig and ipauser modules
- Update of auth_ind choices in ipahost and ipaservice modules
- Upstream test and environment enhancements
- Documentation updates

Changes since 1.11.0
--------------------

- ci: Increase verbosity for Ansible playbook runs (#1123)
- ansible_freeipa_module: Fix ipa_command_invalid_param_choices (#1122)
- Update authtypes authind readmes (#1119)
- Update authtypes authind (#1118)
- ipaserver: Update README with detailed Ubuntu support (#1117)
- utils/run-tests.sh: Install Ansible collections on virtual environment (#1116)
- Remove dependency on 'virtualenv' (#1114)
- Singular to plural on random serial numbers setting (#1106)
- upstream CI: Update ansible-core version (#1100)
- doc: Differentiate location meaning between host and server (#1098)
- Fix handling of ipapwpolicy attributes usercheck and dictcheck (#1076)
- ipaautomountmap: add support for indirect maps (#1075)
- ipauser: Add support for SMB attributes. (#1056)
- ipauser: Support for External IdP attributes. (#1055)
- ipauser: Add support for parameter "street" (#1044)
- ipauser: Add support to modify GECOS field. (#1039)

Detailed changelog since 1.11.0 by author
-----------------------------------------

3 authors, 25 commits

Rafael Guterres Jeffman (14)

- ci: Increase verbosity for Ansible playbook runs
- ipauser: Support for External IdP attributes.
- ipaserver: Update README with detailed Ubuntu support
- ipaautomountmap: add support for indirect maps
- utils/run-tests.sh: Install Ansible collections on virtual environment
- ipauser: Add support for SMB attributes.
- doc: Differentiate location meaning between host and server
- Remove dependency on 'virtualenv'
- ipauser: Add support for parameter "street"
- ipapwpolicy: Updated module documentation.
- ipapwpolicy: Modify handling of usercheck and dictcheck
- module_utils: Export Ansible's 'boolean' parsing function.
- ipauser: Add support to modify GECOS field.
- upstream CI: Update ansible-core version

Renich Bon Ciric (1)

- Singular to plural on random serial numbers setting

Thomas Woerner (10)

- ansible_freeipa_module: Fix ipa_command_invalid_param_choices
- README-user.md: Add choices pkinit, hardened and idp to user_auth_type
- README-service.md: Add choice idp to auth_ind
- README-host.md: Add choice idp to auth_ind
- README-config.md: Add choices pkinit, hardened and idp to user_auth_type
- ipauser: Add choices pkinit, hardened and idp to user_auth_type
- ipaservice: Add choice idp to auth_ind
- ipahost: Add choice idp to auth_ind
- ipaconfig: Add choices pkinit, hardened and idp to user_auth_type
- ansible_freeipa_module: New ipa_command_invalid_param_choices method

Information at GitHub
---------------------
* Release: [1.11.1](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.11.1)
* Tarball: [ansible-freeipa-1.11.1.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.11.1.tar.gz)
