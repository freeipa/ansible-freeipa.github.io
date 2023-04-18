---
layout: home
title: Home
---

ansible-freeipa provides Ansible roles and playbooks to deploy and undeploy FreeIPA servers, replicas and clients, also modules for management.

This repository contains [Ansible](https://www.ansible.com/) roles and playbooks to install and uninstall [FreeIPA](https://www.freeipa.org/) `servers`, `replicas` and `clients`. Also modules for group, host, topology and user management.

**Note**: The Ansible playbooks and roles require a configured Ansible environment where the Ansible nodes are reachable and are properly set up to have an IP address and a working package manager.

## Roles

{% include toc.html path="/documentation/roles/" -%}

## Plugins

{% include toc.html path="/documentation/plugins/" -%}
