#!/usr/bin/env bash
# This is a script to build the Apprainer sif file

set -x
apptainer build --fakeroot streamlit.sif src/streamlit.def