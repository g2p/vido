
# enter-uml

An unprivileged sudo.

`enter-uml` gives you root privileges to interact with a uml kernel of
your choosing.  You may test system calls, filesystems, and some device
drivers without crashing your machine and without root privileges.  This
is also useful if you have root but module loading is restricted.

`enter-uml` does some minimal set up so that your filesystems are reused
— you do not need a root filesystem image — and so that the inner
context is very close to the outer environment.  This makes usage
similar to sudo; your privileges have been raised and you retain access
to the same filesystem environment to run commands from.  Limitations:
there is no network access, and dynamic device node creation is done by
launching udev/eudev by hand.

A suitable kernel can be installed with

    sudo apt-get install user-mode-linux

on Ubuntu and Debian.  You can also download from
<http://uml.devloop.org.uk/kernels.html> or build your own.  If you want
to step inside the kernel, you can use the `--gdb` flag and set
breakpoints before entering.

`enter-uml` requires Python 3.3.

