---
layout: post
title: "ansible-freeipa-1.12.0"
section: Blog
date: 2023-11-24T17:40:00
author: Thomas Woerner
category: release
---

Highlights in 1.12.0
--------------------

- New idoverridegroup management module.
- New idoverrideuser management module.
- New idview management module.
- New idp management module.
- Bug fixes and CI improvements.

Changes since 1.11.1
--------------------

- idoverride{user,group}: Fix delete_continue with state absent (#1176)
- ipahost: Remove dangling dns records during test setup (#1173)
- Update ansible-lint and pylint versions (#1170)
- Reproduce upstream CI groups in developer's machine (#1168)
- upstream CI: Pin ansible-lint version to 6.20 series (#1159)
- ipaidview: Fail to apply unknown (invalid) hosts (#1158)
- upstream CI: Pin Python version to 3.11 (#1157)
- hbacsvcgroup: Remove obsolete result_handler (#1156)
- hbacrule: Fix use of builtin sudo hbacsvcgroup (#1155)
- upstream CI: Fix test selection for CheckPR pipeline. (#1148)
- utils/ansible-freeipa.spec.in: Add ref for idoverridegroup management (#1146)
- Revert "upstream ci: Run nightly tests against Ansible 2.9" (#1145)
- Ensure CI runs against the oldest supported Ansible versions. (#1144)
- Do not use "del os.environ" as the variable might not exist (#1142)
- New idoverridegroup management module. (#1141)
- new_module template fixes (#1140)
- New idoverrideuser management module. (#1139)
- spec file: Updated list of modules (#1138)
- Bump Ansible version to 2.13 (#1136)
- New idview management module. (#1134)
- ipacert: Fix revocation example playbook on README (#1133)
- Updated supported distros (#1131)
- upstream ci: fix sanity test ansible lint failures (#1120)
- Bump linter versions. (#1112)
- New idp management module (#1105)
- upstream CI: Build containers in parallel jobs (#1104)

Detailed changelog since 1.11.1 by author
-----------------------------------------

2 authors, 40 commits

Rafael Guterres Jeffman (28)

- ipahost: Remove dangling dns records during test setup
- utils/run-tests.sh: Replicate Azure's test grouping
- Update ansible-lint and pylint versions
- upstream CI: Build containers in parallel jobs
- upstream ci: Run PR tests using a single job.
- upstream ci: Use a single random seed for spliting tests
- upstream CI: Fix test selection for CheckPR pipeline.
- upstream CI: Pin ansible-lint version to 6.20 series
- upstream CI: Pin Python version to 3.11
- Revert "upstream ci: Run nightly tests against Ansible 2.9"
- upstream ci: Run nightly tests against Ansible 2.9
- upstream ci: Run PR checks against the oldest supported ansible-core
- pylint: Fix redefined-builtin
- pylint: Fix unused-argument
- ci: Bump pylint version
- development: Bump versions of development checks
- pylint: Unnecessary parens after '=' keyword
- Change 'Exception' to 'RuntimeError' when FreeIPA version is too old
- pylint: Disable broad exception warnings
- pylint: Fix warning 'unnecessary "else" after "return"'
- pylint: Disable warning when using non-literal dict
- spec file: Updated list of modules
- ansible-freeipa: Bump minimum supported Ansible version to 2.13
- README-*: Bump minimum supported Ansible version to 2.13
- roles: Bump minimum Ansible version to 2.13
- ansible-lint: Use the same command line as galaxy-importer
- ipacert: Fix revocation example playbook on README
- Updated supported distros

Thomas Woerner (12)

- idoverride{user,group}: Fix delete_continue with state absent
- ipaidview: Fail to apply unknown (invalid) hosts
- hbacsvcgroup: Remove obsolete result_handler
- hbacrule: Fix use of builtin sudo hbacsvcgroup
- utils/ansible-freeipa.spec.in: Add ref for idoverridegroup management
- New idp management module
- New idoverridegroup management module.
- New idoverrideuser management module.
- Do not use "del os.environ" as the variable might not exist
- utils/templates/ipamodule*.py.in: Fix superfluous type in argument spec
- utils/templates/test_module_client_context.yml.in: Fix FQDN issue
- New idview management module.

Information at GitHub
---------------------
* Release: [1.12.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.12.0)
* Tarball: [ansible-freeipa-1.12.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.12.0.tar.gz)
