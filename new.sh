#!/bin/bash

set -e
set -v

if [[ -z $1 ]]; then
    echo "usage $0 packagename"
    exit 1
fi

packagename="$1"

mkdir -p ~/src
cd ~/src
mkdir $packagename
git -C PACKAGE archive master | gzip > $packagename/$packagename.tgz

cd $packagename
tar -xf $packagename.tgz
mv src/PACKAGE src/$packagename

sed -i -e "s/PACKAGE/${packagename}/g" README.md
rm "README.md-e"
for fname in $(find . -name '*.py'); do
    sed -i -e "s/PACKAGE/${packagename}/g" "$fname"
    rm "${fname}-e"
done

rm $packagename.tgz new.sh

git init .
git add .
git commit -m 'first commit'
git tag -a -m '0.1' 0.1
