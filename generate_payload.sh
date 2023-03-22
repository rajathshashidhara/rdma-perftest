entries=${1:-1}
touch payload.dat
dd bs=4 count=${entries} if=/dev/urandom of=payload.dat