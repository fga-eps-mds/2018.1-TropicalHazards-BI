#!/bin/bash

if [ "${TRAVIS_BRANCH}" == "master" ] && [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
    echo "Creating Release package..."
    npx semantic-release
else
    echo "Skipping release"
fi
