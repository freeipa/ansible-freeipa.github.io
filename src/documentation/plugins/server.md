---
layout: page
title: ipaserver
---

Description
-----------

The server module allows to ensure presence and absence of servers. The module requires an existing server, the deployment of a new server can not be done with the module.

Features
--------

* Server management


Supported FreeIPA Versions
--------------------------

FreeIPA versions 4.4.0 and up are supported by the ipaserver module.


Requirements
------------

**Controller**
* Ansible version: 2.13+

**Node**
* Supported FreeIPA version (see above)


Usage
=====

Example inventory file

{% raw %}
```ini
[ipaserver]
ipaserver.test.local
```
{% endraw %}


Example playbook to make sure server "server.example.com" is already present in the topology:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
```
{% endraw %}

This task is not deploying a new server, it is only checking if the server eists. It will therefore fail if the server does not exist.


Example playbook to make sure server "server.example.com" has location mylocation:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      location: mylocation
```
{% endraw %}


Example playbook to make sure server "server.example.com" does not have a location:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      location: ""
```
{% endraw %}


Example playbook to make sure server "server.example.com" has service weight 1:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      service_weight: 1
```
{% endraw %}


Example playbook to make sure server "server.example.com" does not have a service weight:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      service_weight: -1
```
{% endraw %}


Example playbook to make sure server "server.example.com" is hidden:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      hidden: yes
```
{% endraw %}


Example playbook to make sure server "server.example.com" is not hidden:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      hidden: no
```
{% endraw %}


Example playbook to make sure server "server.example.com" is absent from the topology:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      state: absent
```
{% endraw %}


Example playbook to make sure server "server.example.com" is absent from the topology in continuous mode to ignore errors:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      continue: yes
      state: absent
```
{% endraw %}


Example playbook to make sure server "server.example.com" is absent from the topology with skipping the last of role check:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      ignore_last_of_role: yes
      state: absent
```
{% endraw %}


Example playbook to make sure server "server.example.com" is absent from the topology with skipping the topology disconnect check:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      ignore_topology_disconnect: yes
      state: absent
```
{% endraw %}


Example playbook to make sure server "server.example.com" is absent from the domain in force mode even if it does not exist:

{% raw %}
```yaml
---
- name: Playbook to manage IPA server.
  hosts: ipaserver
  become: yes

  tasks:
  - ipaserver:
      ipaadmin_password: SomeADMINpassword
      name: server.example.com
      force: yes
      state: absent
```
{% endraw %}

This task will always report a change.



Variables
---------

Variable | Description | Required
-------- | ----------- | --------
`ipaadmin_principal` | The admin principal is a string and defaults to `admin` | no
`ipaadmin_password` | The admin password is a string and is required if there is no admin ticket available on the node | no
`ipaapi_context` | The context in which the module will execute. Executing in a server context is preferred. If not provided context will be determined by the execution environment. Valid values are `server` and `client`. | no
`ipaapi_ldap_cache` | Use LDAP cache for IPA connection. The bool setting defaults to yes. (bool) | no
`name` \| `cn` | The list of server name strings. | yes
`location` \| `ipalocation_location` | The server DNS location. Only available with 'state: present'. Use "" for location reset. | no
`service_weight` \| `ipaserviceweight` | Weight for server services. Type Values 0 to 65535, -1 for weight reset. Only available with 'state: present'. (int) | no
`hidden` | Set hidden state of a server. Only available with 'state: present'. (bool) | no
`no_members` | Suppress processing of membership attributes. Only avialable with 'state: present'. (bool) | no
`delete_continue` \| `continue` | Continuous mode: Don't stop on errors. Only available with 'state: absent'. (bool) | no
`ignore_last_of_role` | Skip a check whether the last CA master or DNS server is removed. Only available with 'state: absent'. (bool) | no
`ignore_topology_disconnect` | Ignore topology connectivity problems after removal. Only available with 'state: absent'. (bool) | no
`force` | Force server removal even if it does not exist. Will always result in changed. Only available with 'state: absent'. (bool) | no
`state` | The state to ensure. It can be one of `present`, `absent`, default: `present`. `present` is only working with existing servers. | no


Authors
=======

Thomas Woerner
