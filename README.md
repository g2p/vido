
# vido

`vido` is a sudo-like command wrapper that runs commands inside
a lightweight virtual machine.

The main uses are:

- privilege elevation.  Commands run as root even if you don't have
root privileges in the first place.
- quick testing.  Make small changes to the kernel and test them immediately.
- regression testing.  Run the same command against multiple kernels.
- kernel debugging.  There is a `--gdb` flag that will run the virtual
kernel inside a debugger.  If you have an application that triggers
kernel bugs, you can wrap it in `vido --gdb`, usually without changes.

`vido` does some minimal set up so that your filesystems are reused
— you do not need a root filesystem image — and so that the inner
context is very close to the outer environment.

Limitations:

- There is no network access at the moment
- Dynamic device node creation is done by launching udev/eudev by hand

# Requirements

You need Python 3.3

There are two implementations, UML and KVM.
In both cases you need a suitable kernel for the guest.

On Ubuntu and Debian,

    sudo apt-get install user-mode-linux

gets you one.

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

