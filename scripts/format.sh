#!/bin/sh -e
set -x

ruff bot --ignore E501 --fix
black bot