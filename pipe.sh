#!/bin/bash

echo Installing TypeScript
npm install typescript
echo Installing CDK
npm install -g aws-cdk@2.18.0 >/dev/null 2>&1
echo Installing Requirements
pip install -r requirements.txt >/dev/null 2>&1

echo CDK Diff
cdk diff
