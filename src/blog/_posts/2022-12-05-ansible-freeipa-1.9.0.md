---
layout: post
title: "ansible-freeipa-1.9.0"
section: Blog
date: 2022-12-05T04:21:00
author: Thomas Woerner
category: release
---

Highlights in 1.9.0
-------------------

  - New netgroup management module
  - sudorule: Add support for 'hostmask' parameter
  - pwpolicy: Add support for password check and grace limit
  - ipaclient: No kinit on controller for deployment using OTP
  - ipaclient: Configure DNS resolver
  - Support for ansible-core 2.14 tests

Changes since 1.8.4
-------------------

  - tests/azure: Temporarily stay at Ubuntu 20.04 (#1000)
  - environment: Fix os.environ language setting. (#997)
  - ipaclient: No DNS resolver configuration on master (#996)
  - tests/sanity: Add ignore file for ansible-core 2.14 (#992)
  - utils: Remove deprecated shell scripts used to deploy IPA. (#991)
  - pre-commit: Fix pycqa pre-commit repos. (#989)
  - ipaclient: Configure DNS resolver (#988)
  - ipaclient: No kinit on controller for deployment using OTP (#987)
  - github worflows: speed up git checkout. (#986)
  - upstream tests: Removal of 'warn: no' from shell plugins (#984)
  - netgroup: Fix environment cleanup on ipanetgroup tests. (#981)
  - upstream ci: Update Github actions due to old Node.js. (#980)
  - ipaclient_setup_nss: Fix undefined ca_certs for NoCertificateError case (#979)
  - linters: Fix versions of linter packages due to Python 3.11. (#978)
  - Fix ipaserver role for ansible test (#976)
  - Fix ipareplica role for ansible test (#975)
  - Fix upstream ansible test ansible 2.13 (#973)
  - Fix ipaclient role for ansible test (#972)
  - pwpolicy: Add support for password check and grace limit. (#971)
  - Fix ipasmartcard server role for ansible test (#969)
  - Fix ipasmartcard client role for ansible test (#968)
  - ipabackup_get_backup_dir: Fix documentation sections and agument spec (#967)
  - ipamodule_base_docs: Fix documentation sections (#966)
  - ipaconfig: Do not require enable_sid for add_sids or netbios_name (#961)
  - new_module: Modify new_module and templates for Ansible 2.14 (#960)
  - documentation: Change occurences of whitelist to allowlist. (#959)
  - ipavault: Fix documentation sections and agument spec (#958)
  - ipauser: Fix documentation sections and agument spec (#957)
  - ipatrust Fix documentation sections and agument spec (#956)
  - ipatopologysuffix: Fix documentation sections and agument spec (#955)
  - ipatopologysegment: Fix documentation sections and agument spec (#954)
  - ipasudorule: Fix documentation sections and agument spec (#953)
  - ipasudocmdgroup: Fix documentation sections and agument spec (#952)
  - ipasudocmd: Fix documentation sections and agument spec (#951)
  - ipaservicedelegationtarget: Fix documentation sections and agument spec (#950)
  - ipaservicedelegationrule: Fix documentation sections and agument spec (#949)
  - ipaservice:: Fix documentation sections and agument spec (#948)
  - ipaserver: Fix documentation sections and agument spec (#947)
  - ipaselfservice: Fix documentation sections and agument spec (#946)
  - iparole: Fix documentation sections and agument spec (#945)
  - ipapwpolicy: Fix documentation sections and agument spec (#944)
  - ipaprivilege: Fix documentation sections and agument spec (#943)
  - ipapermission: Fix documentation sections and agument spec (#942)
  - ipalocation: Fix documentation sections and agument spec (#941)
  - ipaidrange: Fix documentation sections and agument spec (#940)
  - ipahostgroup: Fix documentation sections and agument spec (#939)
  - ipahost: Fix documentation sections and agument spec (#938)
  - ipahbacsvcgroup: Fix documentation sections and agument spec (#937)
  - ipahbacsvc: Fix documentation sections and agument spec (#936)
  - ipahbacrule: Fix documentation sections and agument spec (#935)
  - ipagroup: Fix documentation sections and agument spec (#934)
  - ipadnszone: Fix documentation sections and agument spec (#933)
  - ipadnsrecord: Fix documentation sections and agument spec (#932)
  - ipadnsforwardzone: : Fix documentation sections and agument spec (#931)
  - ipadnsconfig: Fix documentation sections and agument spec (#930)
  - ipadelegation: : Fix documentation sections and agument spec (#929)
  - ipaconfig: Fix documentation sections and agument spec (#928)
  - ipaautomountmap: Fix documentation sections and agument spec (#927)
  - ipaautomountlocation: Fix documentation sections and agument spec (#926)
  - ipaautomountkey: Fix documentation sections and agument spec (#925)
  - ipaautomember: Fix documentation sections and agument spec (#924)
  - sudorule: Add support for 'hostmask' parameter (#922)
  - ipaconfig: Do not allow enable_sid set to False. (#921)
  - ipaconfig: Fix fail_json calls. (#920)
  - Fix plugins for ansible fake execution test (#918)
  - ipabackup_get_backup_dir: Fix for ansible-test fake execution test (#917)
  - ipasmartcard_client_get_vars: Fix for ansible-test fake execution test (#916)
  - ipasmartcard_server_get_vars: Fix for ansible-test fake execution test (#915)
  - Re-enable dnsforwardzone tests (#914)
  - ansible_freeipa_module: Remove deprecated FreeIPABaseModule (#913)
  - New netgroup management module (#875)

Detailed changelog since 1.8.4 by author
----------------------------------------
  3 authors, 142 commits

Denis Karpelevich (1)

  - New netgroup management module

Rafael Guterres Jeffman (22)

  - tests/sanity: Add ignore file for ansible-core 2.14
  - environment: Fix os.environ language setting.
  - utils: Remove deprecated shell scripts used to deploy IPA.
  - pre-commit: Fix pycqa pre-commit repos.
  - sudorule: Add support for 'hostmask' parameter
  - github worflows: speed up git checkout.
  - pwpolicy: Add support for password check and grace limit.
  - upstream tests: Removal of 'warn: no' from shell plugins
  - upstream ci: Use Shellcheck action from 'master'.
  - upstream ci: Update Github actions due to old Node.js.
  - pylint: Fix pylint issues on utils/galaxyfy-module-EXAMPLES.py
  - pylint: Update configuration for Python 3.11
  - pylint: Modify certificate loader function definition.
  - linters: Fix versions of linter packages due to Python 3.11.
  - netgroup: Fix environment cleanup on ipanetgroup tests.
  - documentation: Change occurences of whitelist to allowlist.
  - ipaconfig: Do not require enable_sid for add_sids or netbios_name
  - ipaconfig: Do not allow enable_sid set to False.
  - new_module: Modify new_module and templates for Ansible 2.14
  - ipaconfig: Fix fail_json calls.
  - Azure CI: Re-enable dnszone tests with forwarder ports
  - Azure CI: Update variable files instructions.

Thomas Woerner (119)

  - tests/azure: Temporarily stay at Ubuntu 20.04
  - ipaclient: No DNS resolver configuration on master
  - ipaclient: No kinit on controller for deployment using OTP
  - ipaclient: Configure DNS resolver
  - ipaserver_test: Fix documentation sections and agument spec
  - ipaserver_setup_otpd: Fix documentation sections and agument spec
  - ipaserver_setup_ntp: Fix documentation sections and agument spec
  - ipaserver_setup_krb: Fix documentation sections and agument spec
  - ipaserver_setup_kra: Fix documentation sections and agument spec
  - ipaserver_setup_http: Fix documentation sections and agument spec
  - ipaserver_setup_ds: Fix documentation sections and agument spec
  - ipaserver_setup_dns: Fix documentation sections and agument spec
  - ipaserver_setup_custodia: Fix documentation sections and agument spec
  - ipaserver_setup_ca: Fix documentation sections and agument spec
  - ipaserver_setup_adtrust: Fix documentation sections and agument spec
  - ipaserver_set_ds_password: Fix documentation sections and agument spec
  - ipaserver_prepare: Fix documentation sections and agument spec
  - ipaserver_master_password: Fix documentation sections and agument spec
  - ipaserver_load_cache: Fix documentation sections and agument spec
  - ipaserver_enable_ipa: Fix documentation sections and agument spec
  - ansible_ipa_server: Fix ansible-test fake execution test findings
  - ipareplica_test: Fix documentation sections and agument spec
  - ipareplica_setup_otpd: Fix documentation sections and agument spec
  - ipareplica_setup_krb: Fix documentation sections and agument spec
  - ipareplica_setup_kra: Fix documentation sections and agument spec
  - ipareplica_setup_http: Fix documentation sections and agument spec
  - ipareplica_setup_ds: Fix documentation sections and agument spec
  - ipareplica_setup_dns: Fix documentation sections and agument spec
  - ipareplica_setup_custodia: Fix documentation sections and agument spec
  - ipareplica_setup_certmonger: Fix documentation sections and agument spec
  - ipareplica_setup_ca: Fix documentation sections and agument spec
  - ipareplica_setup_adtrust: Fix documentation sections and agument spec
  - ipareplica_restart_kdc: Fix documentation sections and agument spec
  - ipareplica_promote_sssd: Fix documentation sections and agument spec
  - ipareplica_promote_openldap_conf: Fix documentation sections and agument spec
  - ipareplica_prepare: Fix documentation sections and agument spec
  - ipareplica_master_password: Fix documentation sections and agument spec
  - ipareplica_krb_enable_ssl: Fix documentation sections and agument spec
  - ipareplica_install_ca_certs: Fix documentation sections and agument spec
  - ipareplica_enable_ipa: Fix documentation sections and agument spec
  - ipareplica_ds_enable_ssl: Fix documentation sections and agument spec
  - ipareplica_ds_apply_updates: Fix documentation sections and agument spec
  - ipareplica_custodia_import_dm_password: Fix doc sections and agument spec
  - ipareplica_create_ipa_conf: Fix documentation sections and agument spec
  - ipareplica_add_to_ipaservers: Fix documentation sections and agument spec
  - ansible_ipa_replica: Fix ansible-test fake execution test findings
  - ipaclient_test_keytab: Fix documentation sections and agument spec
  - ipaclient_test: Fix documentation sections and agument spec
  - ipaclient_setup_sssd: Fix documentation sections and agument spec
  - ipaclient_setup_ssh: Fix documentation sections and agument spec
  - ipaclient_setup_ntp: Fix documentation sections and agument spec
  - ipaclient_setup_nss: Fix documentation sections and agument spec
  - ipaclient_setup_nis: Fix documentation sections and agument spec
  - ipaclient_setup_krb5: Fix documentation sections and agument spec
  - ipaclient_setup_firefox: Fix documentation sections and agument spec
  - ipaclient_setup_automount: Fix documentation sections and agument spec
  - ipaclient_set_hostname: Fix documentation sections and agument spec
  - ipaclient_join: Fix documentation sections and agument spec
  - ipaclient_ipa_conf: Fix documentation sections and agument spec
  - ipaclient_get_otp: Fix documentation sections and agument spec
  - ipaclient_get_facts: Fix documentation sections and agument spec
  - ipaclient_fstore: Fix documentation sections and agument spec
  - ipaclient_fix_ca: Fix documentation sections and agument spec
  - ipaclient_api: Fix documentation sections and agument spec
  - ansible_ipa_client: Fix ansible-test fake execution test findings
  - ipaclient_setup_nss: Fix undefined ca_certs for NoCertificateError case
  - tests/sanity/sanity.sh: shellcheck: Fix command for use_docker
  - tests/sanity: New tests/sanity/ignore-2.13.txt for ansible-test
  - ipasmartcard_server_validate_ca_certs: Fix doc sections and agument spec
  - ipasmartcard_server_get_vars: Fix doc sections and agument spec
  - ipasmartcard_client_validate_ca_certs: Fix doc sections and agument spec
  - ipasmartcard_client_get_vars: Fix doc sections and agument spec
  - ipabackup_get_backup_dir: Fix documentation sections and agument spec
  - ipamodule_base_docs: Fix documentation sections
  - ipadnsrecord: Fix documentation sections and agument spec
  - ipahost: Fix documentation sections and agument spec
  - ipatopologysegment: Fix documentation sections and agument spec
  - README-vault: Add new_public_key and new_public_key_file
  - ipavault: Fix documentation sections and agument spec
  - ipauser: Fix documentation sections and agument spec
  - ipatrust Fix documentation sections and agument spec
  - ipatopologysuffix: Fix documentation sections and agument spec
  - ipasudorule: Fix documentation sections and agument spec
  - ipasudocmdgroup: Fix documentation sections and agument spec
  - ipasudocmd: Fix documentation sections and agument spec
  - ipaservicedelegationtarget: Fix documentation sections and agument spec
  - ipaservicedelegationrule: Fix documentation sections and agument spec
  - ipaservice:: Fix documentation sections and agument spec
  - ipaserver: Fix documentation sections and agument spec
  - ipaselfservice: Fix documentation sections and agument spec
  - iparole: Fix documentation sections and agument spec
  - ipapwpolicy: Fix documentation sections and agument spec
  - ipaprivilege: Fix documentation sections and agument spec
  - ipapermission: Fix documentation sections and agument spec
  - ipalocation: Fix documentation sections and agument spec
  - ipaidrange: Fix documentation sections and agument spec
  - ipahostgroup: Fix documentation sections and agument spec
  - ipahbacsvcgroup: Fix documentation sections and agument spec
  - ipahbacsvc: Fix documentation sections and agument spec
  - ipahbacrule: Fix documentation sections and agument spec
  - ipagroup: Fix documentation sections and agument spec
  - ipadnszone: Fix documentation sections and agument spec
  - ipadnsforwardzone: : Fix documentation sections and agument spec
  - ipadnsconfig: Fix documentation sections and agument spec
  - ipadelegation: : Fix documentation sections and agument spec
  - ipaconfig: Fix documentation sections and agument spec
  - ipaautomountmap: Fix documentation sections and agument spec
  - ipaautomountlocation: Fix documentation sections and agument spec
  - ipaautomountkey: Fix documentation sections and agument spec
  - ipaautomember: Fix documentation sections and agument spec
  - tests/sanity/ignore-2.12.txt: Remove unnecessary entries
  - ipadnszone: import netaddr and DNSName from ansible_freeipa_module
  - ipadnsrecord: Fix for ansible-test fake execution test
  - ansible_freeipa_module: Fix ansible-test fake execution test findings
  - ipabackup_get_backup_dir: Fix for ansible-test fake execution test
  - ipasmartcard_client_get_vars: Fix for ansible-test fake execution test
  - ipasmartcard_server_get_vars: Fix for ansible-test fake execution test
  - tests/sanity/ignore-2.12.txt: Remove ansible-deprecated-no-collection-name
  - ansible_freeipa_module: Remove deprecated FreeIPABaseModule

Information at GitHub
---------------------
* Release: [1.9.0](https://github.com/freeipa/ansible-freeipa/releases/tag/v1.9.0)
* Tarball: [ansible-freeipa-1.9.0.tar.gz](https://github.com/freeipa/ansible-freeipa/archive/refs/tags/v1.9.0.tar.gz)
