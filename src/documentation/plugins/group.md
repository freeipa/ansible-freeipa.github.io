---
layout: page
title: ipagroup
---

Description
-----------

The group module allows to ensure presence and absence of groups and members of groups.

The group module is as compatible as possible to the Ansible upstream `ipa_group` module, but additionally offers to add users to a group and also to remove users from a group.

## Note
Ensuring presence (adding) of several groups with mixed types (`external`, `nonposix` and `posix`) requires a fix in FreeIPA. The module implements a workaround to automatically use `client` context if the fix is not present in the target node FreeIPA and if more than one group is provided to the task using the `groups` parameter. If `ipaapi_context` is forced to be `server`, the module will fail in this case.


Features
--------
* Group management


Supported FreeIPA Versions
--------------------------

FreeIPA versions 4.4.0 and up are supported by the ipagroup module.

Some variables are only supported on newer versions of FreeIPA. Check `Variables` section for details.


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


Example playbook to add groups:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver
  become: true

  tasks:
  # Create group ops with gid 1234
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: ops
      gidnumber: 1234

  # Create group sysops
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: sysops
      user:
      - pinky

  # Create group appops
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: appops
```
{% endraw %}

These three `ipagroup` module calls can be combined into one with the `groups` variable:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver

  tasks:
  - name: Ensure groups ops, sysops and appops are present
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      groups:
      - name: ops
        gidnumber: 1234
      - name: sysops
        user:
        - pinky
      - name: appops
```
{% endraw %}

You can also alternatively use a json file containing the groups, here `groups_present.json`:

{% raw %}
```json
{
  "groups": [
    {
      "name": "group1",
      "description": "description group1"
    },
    {
      "name": "group2",
      "description": "description group2"
    }
  ]
}
```
{% endraw %}

And ensure the presence of the groups with this example playbook:

{% raw %}
```yaml
---
- name: Tests
  hosts: ipaserver
  gather_facts: false

  tasks:
  - name: Include groups_present.json
    include_vars:
      file: groups_present.json

  - name: Groups present
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      groups: "{{ groups }}"
```
{% endraw %}

Example playbook to rename a group:

{% raw %}
```yaml
---
- name: Playbook to rename a single group
  hosts: ipaserver
  become: false
  gather_facts: false

  tasks:
  - name: Rename group appops to webops
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: appops
      rename: webops
      state: renamed
```
{% endraw %}

Several groups can also be renamed with a single task, as in the example playbook:

{% raw %}
```yaml
---
- name: Playbook to rename multiple groups
  hosts: ipaserver
  become: false
  gather_facts: false

  tasks:
  - name Rename group1 to newgroup1 and group2 to newgroup2
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      groups:
      - name: group1
        rename: newgroup1
      - name: group2
        rename: newgroup2
      state: renamed
```
{% endraw %}

Example playbook to add users to a group:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver
  become: true

  tasks:
  # Add user member brain to group sysops
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: sysops
      action: member
      user:
      - brain
```
{% endraw %}
`action` controls if a the group or member will be handled. To add or remove members, set `action` to `member`.


Example playbook to add group members to a group:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver
  become: true

  tasks:
  # Add group members sysops and appops to group ops
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: ops
      group:
      - sysops
      - appops
```
{% endraw %}

Example playbook to add members from a trusted realm to an external group:

{% raw %}
```yaml
---
- name: Playbook to handle groups.
  hosts: ipaserver
  
  tasks:
  - name: Create an external group and add members from a trust to it.
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: extgroup
      external: yes
      externalmember:
      - WINIPA\\Web Users
      - WINIPA\\Developers
```
{% endraw %}

Example playbook to add nonposix and external groups:

{% raw %}
```yaml
---
- name: Playbook to add nonposix and external groups
  hosts: ipaserver

  tasks:
  - name: Add nonposix group sysops and external group appops
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      groups:
      - name: sysops
        nonposix: true
      - name: appops
        external: true
```
{% endraw %}

Example playbook to remove groups:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver
  become: true

  tasks:
  # Remove groups sysops, appops and ops
  - ipagroup:
      ipaadmin_password: SomeADMINpassword
      name: sysops,appops,ops
      state: absent
```
{% endraw %}

Example playbook to ensure groups are absent:

{% raw %}
```yaml
---
- name: Playbook to handle groups
  hosts: ipaserver

  tasks:
  - name: Ensure groups ops and sysops are absent
    ipagroup:
      ipaadmin_password: SomeADMINpassword
      groups:
      - name: ops
      - name: sysops
      state: absent
```
{% endraw %}

Variables
=========

Variable | Description | Required
-------- | ----------- | --------
`ipaadmin_principal` | The admin principal is a string and defaults to `admin` | no
`ipaadmin_password` | The admin password is a string and is required if there is no admin ticket available on the node | no
`ipaapi_context` | The context in which the module will execute. Executing in a server context is preferred. If not provided context will be determined by the execution environment. Valid values are `server` and `client`. | no
`ipaapi_ldap_cache` | Use LDAP cache for IPA connection. The bool setting defaults to <br/>. (bool) | no
`name` \| `cn` | The list of group name strings. | no
`groups` | The list of group dicts. Each `groups` dict entry can contain group variables.<br>There is one required option in the `groups` dict:| no
&nbsp; | `name` - The group name string of the entry. | yes
`description` | The group description string. | no
`gid` \| `gidnumber` | The GID integer. | no
`posix` | Create a non-POSIX group or change a non-POSIX to a posix group. `nonposix`, `posix` and `external` are mutually exclusive. (bool) | no
`nonposix` | Create as a non-POSIX group. `nonposix`, `posix` and `external` are mutually exclusive. (bool) | no
`external` | Allow adding external non-IPA members from trusted domains. `nonposix`, `posix` and `external` are mutually exclusive. (bool) | no
`nomembers` | Suppress processing of membership attributes. (bool) | no
`user` | List of user name strings assigned to this group. | no
`group` | List of group name strings assigned to this group. | no
`service` | List of service name strings assigned to this group. Only usable with IPA versions 4.7 and up. | no
`membermanager_user` | List of member manager users assigned to this group. Only usable with IPA versions 4.8.4 and up. | no
`membermanager_group` | List of member manager groups assigned to this group. Only usable with IPA versions 4.8.4 and up. | no
`externalmember` \| `ipaexternalmember`  \| `external_member`| List of members of a trusted domain in DOM\\name or name@domain form. | no
`idoverrideuser` | List of user ID overrides to manage. Only usable with IPA versions 4.8.7 and up.| no
`rename` \| `new_name` | Rename the user object to the new name string. Only usable with `state: renamed`. | no
`action` | Work on group or member level. It can be on of `member` or `group` and defaults to `group`. | no
`state` | The state to ensure. It can be one of `present`, `absent` or `renamed`, default: `present`. | yes


Authors
=======

- Thomas Woerner
- Rafael Jeffman
