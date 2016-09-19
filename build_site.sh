#!/bin/sh

DIR=$(mktemp -d)
git clone https://github.com/adamhammes/hammes.io $DIR
cd $DIR
jekyll build --incremental --destination /home/adam/site
rm -rf $DIR
