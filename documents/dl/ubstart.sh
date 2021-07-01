#!/bin/bash

kvm \
-m 4096 \
-smp 4 \
-drive file=$HOME/Downloads/Xubuntu18.qcow2,if=virtio \
-net user,hostfwd=tcp::7777-:22 \
-net nic,model=virtio \
-vga virtio
