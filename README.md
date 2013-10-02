
# vido

`vido` is a kernel launcher.  It is used much like sudo, by putting
`vido --` in front of a command.
Commands run inside a new kernel, with passthrough access
to the filesystem, whitelisted devices, and (if enabled) the network.

The main uses are:

- **Privilege virtualisation.**  `vido` starts out entirely unprivileged,
  and creates an environment where commands run as root without affecting
  the rest of the system.  This is a more powerful alternative to `fakeroot`;
  it allows full access to a possibly customised kernel.
- **Regression testing.**  Run the same command against multiple kernels.
- **Kernel debugging.**  The `--gdb` flag runs the virtual
  kernel inside a debugger.  If you have an application that
  triggers kernel bugs, you can wrap it in `vido --gdb`, usually
  without changes.
- **Kernel hacking.**  Experiment with small changes to the kernel
  and test them immediately.

Get overlay access to privileged directories with `--clear-dirs`
and `--rw-dirs` (the latter requires the overlayfs kernel patchset).

Pass disk images or block devices with `--disk`.
They are exposed as `$VIDO_DISK0`… variables.

Aside from the default pass-throughs, commands run in a fairly
bare environment.  If more services are needed, pass a script
that will launch them.  For example, launching udev/eudev gives
udev support.

With network passthrough (`--net`), commands can do unprivileged
networking (a SLIRP stack, with IPv4 NAT).  The `ping` command won't work
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
In both cases you need a suitable kernel for the guest.

## UML

On Ubuntu and Debian,

    sudo apt-get install user-mode-linux

installs a UML kernel which you can run with:

    vido --uml

You can also download UML kernels from
<http://uml.devloop.org.uk/kernels.html>, or build your own:

    vido --uml --kernel path/to/linux

## Qemu / KVM

You may be able to use your current kernel:

    vido --kvm --qemu-9p-workaround --watchdog

This is designed to work with distribution kernels that don't
have 9p modules built-in.
`--qemu-9p-workaround` is required if Qemu is older than 1.6.

If the distribution kernel isn't suitable, build a minimal kernel with:

    CONFIG_NET_9P=y
    CONFIG_NET_9P_VIRTIO=y
    CONFIG_9P_FS=y
    CONFIG_DEVTMPFS=y
    CONFIG_SERIAL_8250_CONSOLE=y

Note that 9p can't be built as a loadable module, it has to be built in.
Your kernel should also have:

    CONFIG_DEVTMPFS_MOUNT=y
    CONFIG_9P_FSCACHE=y
    # networking
    CONFIG_E1000=y
    CONFIG_PACKET=y
    # watchdog
    CONFIG_IB700_WDT=y

Usage:

    vido --kvm --kernel path/to/arch/x86/boot/bzImage

## User namespaces

As an alternative to UML and KVM, `vido` can also use user namespaces.
This is a recent kernel feature, less powerful than kernel
virtualisation (you become root, but without the ability to take
over the kernel and without many unvirtualised kernel features) but
powerful enough to allow some control over mountpoints.


