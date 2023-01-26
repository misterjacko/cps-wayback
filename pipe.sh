#!/bin/bash

echo Installing TypeScript...
npm install typescript

echo Silently installing CDK...
npm install -g aws-cdk@2.18.0 >/dev/null 2>&1
cdk --version

echo Silently installing Requirements...
pip install -r requirements.txt >/dev/null 2>&1

echo Running CDK Diff
cdk diff
