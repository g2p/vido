#!/usr/bin/env python3.3
# encoding: utf-8

from distutils.core import setup

setup(
    name='vido',
    version='0.3.0',
    author='Gabriel de Perthuis',
    author_email='g2p.code+vido@gmail.com',
    url='https://github.com/g2p/vido',
    license='GNU GPL',
    keywords=
        'kvm uml debugging testing ci gdb virtualisation '
        'sudo unshare fakeroot wrapper',
    description='Wrap commands in throwaway virtual machines',
    scripts=['vido', 'virt-stub'],
    classifiers='''
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        License :: OSI Approved :: GNU General Public License (GPL)
        Operating System :: POSIX :: Linux
        Topic :: Utilities
        Environment :: Console
    '''.strip().splitlines(),
    long_description='''
    vido is a sudo-like command wrapper.  Commands run inside a new
    kernel, with passthrough access to the filesystem, whitelisted
    devices, and (if enabled) the network.

    The main uses are:

    * Experimentation.  Make small changes to the kernel and test them
      immediately.
    * Privilege elevation.  Commands run as root even if you don't have
      root privileges in the first place.
    * Regression testing.  Run the same command against multiple kernels.
    * Kernel debugging.  The --gdb flag will run the virtual kernel
      inside a debugger.

    See `github.com/g2p/vido <https://github.com/g2p/vido#readme>`_
    for installation and usage instructions.''')

