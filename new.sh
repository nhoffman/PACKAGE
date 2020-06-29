#!/bin/bash

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
rm $packagename.tgz
mv PACKAGE.py $packagename.py
mv PACKAGE $packagename
rm new.sh
fd \\.py | xargs -I XXX sed -i -e "s/PACKAGE/${packagename}/g" XXX
fd \\-e | xargs rm
git init .
git add .
git commit -m 'first commit'
git tag -a -m '0.1' 0.1
