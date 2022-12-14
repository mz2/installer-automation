#!/bin/bash

set -e pipefail

if [ -f ./vm/kinetic.qcow2 ]; then
  echo "kinetic VM already exists at ./vm/kinetic.qcow2. Remove it and try again."
  exit 1
fi

if [ ! -f ./kinetic-desktop-canary-amd64.iso ]; then
  echo "Missing ./kinetic-desktop-canary-amd64.iso (symlink it in, please, and try again)."
  exit 1
fi

if [ -z "${SIKULIX_JAR}" ]; then
  echo "Missing 'SIKULIX_JAR' environment variable (point it at your sikulixide jar, please, and try again)."
  exit 1
fi 

mkdir -p vm
sleep 1
quickemu --vm kinetic.conf

java -jar $SIKULIX_JAR -r installer-automation.sikuli
SIKULI_EXIT = $?

set +e +pipefail
killall qemu-system-x86_64 || /bin/true

exit $SIKULI_EXIT
