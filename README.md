
# vido

`vido` is a sudo-like command wrapper.
Commands run inside a new kernel, with passthrough access
to the filesystem, whitelisted devices, and (if enabled) the network.

The main uses are:

- **Experimentation.**  Make small changes to the kernel and test
  them immediately.
- **Privilege elevation.**  Commands run as root even if you don't
  have root privileges in the first place.  This is a more powerful
  alternative to `fakeroot` which lets you mount filesystems and use
  arbitrary kernel features.
- **Regression testing.**  Run the same command against multiple
  kernels.
- **Kernel debugging.**  The `--gdb` flag will run the virtual
  kernel inside a debugger.  If you have an application that
  triggers kernel bugs, you can wrap it in `vido --gdb`, usually
  without changes.

If services are needed, launching them is your responsibility.

- If you need udev/eudev, run them manually
- If network passthrough is enabled, you get unprivileged networking
  (a SLIRP stack, with IPv4 NAT).  The `ping` command won't work
  unless [patched](http://openwall.info/wiki/people/segoon/ping#Userspace-support)
  to use [ICMP sockets](https://lwn.net/Articles/420799/).

# Usage

The default command is a shell:

    vido

Always put two dashes before the command:

    vido -- cat /proc/uptime
    vido -- sh -c 'dmesg |tail'

Most flags should be self-documenting:

    vido --help

# Requirements

You need Python 3.3

There are two main implementations, UML and KVM.
The KVM implementation is more feature complete, but the kernel
binary needs to be built with some non-default options.
In both cases you need a suitable kernel for the guest.

On Ubuntu and Debian,

    sudo apt-get install user-mode-linux

gets you a UML kernel.

You can also download UML kernels from
<http://uml.devloop.org.uk/kernels.html> or build your own.
Use the `--kernel <path/to/linux>` flag in this case.

If you want to run inside Qemu/KVM, pass the `--kvm` flag.
Your kernel needs to be built with:

    CONFIG_NET_9P=y
    CONFIG_NET_9P_VIRTIO=y
    CONFIG_9P_FS=y
    CONFIG_9P_FS_POSIX_ACL=y

Note that 9p can't be built as a module, it has to be linked in.

Network support requires the following:

    CONFIG_E1000=y
    CONFIG_PACKET=y

As an alternative to UML and KVM, vido can also use user namespaces.
This is a recent kernel feature, less powerful than kernel
virtualisation (you become root, but without the ability to take
over the kernel and without many unvirtualised kernel features) but
powerful enough to allow mounting arbitrary filesystems.


