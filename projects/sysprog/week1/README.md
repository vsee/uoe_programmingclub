# Environment Setup

We want a common development platform.
We do system programming, including kernel-space programming where your OS
kernel can crash and you need to reboot the computer if you write wrong code
(e.g., NULL pointer dereference).
We thus run our code inside a virtual machine (VM) to protect your host
system.

We use [Virtualbox](https://www.virtualbox.org/) as the virtualization software because it works in most of the Linux distributions, Windows and Mac.
To ease the VM control, we also use [Vagrant](https://www.vagrantup.com/).
We use [Debian](https://www.debian.org/) for convenience of the development;
Ubuntu would be slightly more popular, but that on Virtualbox has a problem with serial console, which is often needed for kernel debugging.

## 1. Install Virtualbox and Vagrant
Install [Virtualbox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/).

## 2. Launch a VM
Start a terminal (Linux/Mac) or command prompt (Windows)
```
mkdir progclub
cd progclub
```
Put a file called [Vagrantfile](./Vagrantfile) in the progclub directory
```
vagrant up
```
You can log into the VM from the Virtualbox window or command line in the
progclub directory (user/pass is vagrant/vagrant):
```
vagrant ssh
```
(optional) You can also ssh to the VM from elsewhere
```
vagrant ssh --host myvm >> ~/.ssh/config
ssh myvm
```

## 3. Provision the VM
```
sudo apt-get update
sudo apt-get install build-essential git vim-nox linux-headers-4.19.0-9-amd64
```

## 4. Hello World in the OS kernel
```
git clone https://github.com/micchie/hellokernel.git
cd hellokernel
make
sudo insmod ./hello.ko
sudo dmesg
```
Now you loaded your custom kernel module.
You should see "Hello world!" at the bottom of the output.
Let's unload it for now.
```
sudo rmmod hello
```
Shutdown the VM (in the progclub directory of your host computer (i.e., NOT in the VM)
```
vagrant halt
```
You can also destroy the VM
```
vagrant destroy
```
