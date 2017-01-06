#!/bin/bash

echo -en "travis_fold:start:url\r"
echo "########################################################################"
echo "########################################################################"
echo "http://travisatfluid.s3-website-us-east-1.amazonaws.com/training/$TRAVIS_BUILD_NUMBER/$TRAVIS_JOB_NUMBER/people/"
echo "########################################################################"
echo "########################################################################"
echo -en "travis_fold:end:url\r"
