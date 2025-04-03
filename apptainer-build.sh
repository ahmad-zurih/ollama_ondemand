#!/usr/bin/env bash
# This is a script to build the Apptainer sif file

set -x
cd src
apptainer build --fakeroot --force ../streamlit_with_ollama.sif streamlit_with_ollama.def