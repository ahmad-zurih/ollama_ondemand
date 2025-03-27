#!/usr/bin/env bash
# This is a script to build the Apptainer sif file

set -x
cd src
apptainer build --fakeroot ../streamlit.sif streamlit.def