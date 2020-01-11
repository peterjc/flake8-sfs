#!/bin/bash
IFS=$'\n\t'
set -eu

# Examples which should fail
for code in SFS??? ; do
    echo "======"
    echo $code
    echo "======"
    for file in $code/*.py ; do
        echo "flake8 --select SFS $file"
        flake8 --select SFS $file 2>&1 | grep ": $code "
    done
    echo "Good, $code violations reported, as expected."
done
# echo "Positive tests passed (SFS errors reported as expected)."

echo "============"
echo "Tests passed"
echo "============"
