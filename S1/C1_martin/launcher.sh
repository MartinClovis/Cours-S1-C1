#!/bin/bash
source .venv/bin/activate
flask --debug  --app app  run   --host 0.0.0.0
