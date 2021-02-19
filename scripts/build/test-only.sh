#!/bin/bash
set -e

usage()
{
    echo "Usage: $0 [<options>] <pip-install-str>"
    echo "Sample: $0 --python /usr/bin/python37 'pypylon==1.7.0rc2'"
    echo "Options:"
    echo "  --python <path to binary>                 Use the given python binary"
    echo "  -h                                        This usage help"
}

PYTHON="python"
PIP_INSTALL_STR=""

# parse args
while [ $# -gt 1 ]; do
    arg="$1"
    case $arg in
        --python) PYTHON="$2" ; shift ;;
        -h|--help) usage ; exit 1 ;;
        *)         echo "Unknown argument $arg" ; usage ; exit 1 ;;
    esac
    shift
done

PIP_INSTALL_STR="$1"


BASEDIR="$(cd $(dirname $0)/../.. ; pwd)"
#enter source dir
pushd $BASEDIR
pwd

$PYTHON -m pip install --user 'pip>=20.3'
$PYTHON -m pip install --user numpy
$PYTHON -m pip install --user "$PIP_INSTALL_STR"
$PYTHON tests/all_emulated_tests.py

popd


