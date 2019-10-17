#!/bin/bash
neuroapi run -h 0.0.0.0 >/dev/null 2>&1 &
disown -h
