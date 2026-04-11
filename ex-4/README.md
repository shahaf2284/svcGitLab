# Exercise 4 - Ansible Installation Based on Docker

## Exercise Description

Set up an Ansible environment using Docker containers. The goal is to create two containers — an **Ansible Master** and an **Ansible Slave** — and verify connectivity between them using Ansible's ping module.

### Highlight Steps

1. Run an `ansible-slave` Docker container
2. Configure it correctly (SSH server, user credentials)
3. Run an `ansible-master` Docker container
4. Configure it correctly (Ansible, SSH client, inventory)
5. Create an inventory configuration file

### Test via Ansible Ping

From the master container, run:

```bash
ansible -m ping all
```

**Expected output:**

```
10.132.0.41 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

## Solution

### Project Structure

```
ex-4/
├── master/
│   ├── dockerfile
│   ├── ansible.cfg
│   └── inventory
├── slave/
│   └── Dockerfile
└── ex-4.pdf
```

---

### Slave Container

**`slave/Dockerfile`**

```dockerfile
FROM ubuntu:22.04
RUN apt update && apt install -y openssh-server
RUN mkdir /var/run/sshd
RUN useradd -m slave && echo "slave:2284" | chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
```

**What it does:**
- Based on Ubuntu 22.04
- Installs OpenSSH server
- Creates a user `slave` with password `2284`
- Exposes port 22 for SSH connections
- Runs the SSH daemon in the foreground

**Build & Run:**

```bash
docker build -t ansible-slave ./slave
docker run -d --name ansible-slave ansible-slave
```

---

### Master Container

**`master/dockerfile`**

```dockerfile
FROM ubuntu:22.04
RUN apt update && apt install -y ansible
RUN apt install -y openssh-client sshpass
WORKDIR /app
COPY inventory /etc/ansible/hosts
COPY ansible.cfg /etc/ansible/ansible.cfg
CMD ["bash"]
```

**What it does:**
- Based on Ubuntu 22.04
- Installs Ansible, OpenSSH client, and `sshpass` (for password-based SSH authentication)
- Copies the inventory and Ansible config into the container
- Opens a bash shell for interactive use

**`master/ansible.cfg`**

```ini
[defaults]
inventory = /etc/ansible/hosts
host_key_checking = False
```

- Points Ansible to the inventory file
- Disables host key checking (needed for automated SSH in containers)

**`master/inventory`**

```ini
[servers]
ansible-slave ansible_user=slave ansible_password=2284
```

- Defines a group `[servers]` with the slave container as a host
- Uses the credentials created in the slave Dockerfile

**Build & Run:**

```bash
docker build -t ansible-master ./master
docker run -it --name ansible-master --link ansible-slave ansible-master
```

> **Note:** The `--link` flag connects the master container to the slave container so that the hostname `ansible-slave` resolves correctly.

---

### Testing the Setup

Once inside the master container, run:

```bash
ansible -m ping all
```

A successful response confirms that the master can reach and authenticate with the slave via SSH:

```
ansible-slave | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

## Summary

| Component | Role | Key Packages |
|-----------|------|-------------|
| `ansible-slave` | Target host (SSH server) | `openssh-server` |
| `ansible-master` | Control node (Ansible) | `ansible`, `openssh-client`, `sshpass` |

This exercise demonstrates how to set up a minimal Ansible lab environment using Docker, where the master node manages the slave node over SSH.

