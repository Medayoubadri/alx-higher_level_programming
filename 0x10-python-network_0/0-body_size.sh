#!/bin/bash
# Displays the size of the body of the response of a curl request
curl -s "$1" | wc -c
