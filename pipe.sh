#!/bin/bash

npm install typescript
npm install -g aws-cdk@2.18.0 >/dev/null 2>&1
pip install -r requirements.txt >/dev/null 2>&1
cdk --version
ls
cdk diff
