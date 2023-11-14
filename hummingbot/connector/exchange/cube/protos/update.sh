#!/bin/bash
#
# This updates the protobufs in this directory by pulling them from Cube Exchanges community repository.
#
# azoth zephyr <azoth@zephyr.sx>

git clone git@github.com:cubexch/community.git
cp community/sdk/python/* ./
rm -rf community
