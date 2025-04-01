#!/bin/bash

# Usage: ./bump-version.sh NEW_VERSION
# Example: ./bump-version.sh 2.1

if [ $# -ne 1 ]; then
    echo "Usage: $0 NEW_VERSION"
    echo "Example: $0 2.1"
    exit 1
fi

NEW_VERSION=$1
CURRENT_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$0")

# Navigate to script directory if different from current
if [ "$CURRENT_DIR" != "$SCRIPT_DIR" ]; then
    cd "$SCRIPT_DIR"
fi

# Extract current version from server.py
CURRENT_VERSION=$(grep 'VERSION = ' server.py | cut -d '"' -f 2)

echo "Bumping version from $CURRENT_VERSION to $NEW_VERSION"

# Update version in server.py
sed -i "" "s/VERSION = \"$CURRENT_VERSION\"/VERSION = \"$NEW_VERSION\"/" server.py

# Update version in compose.yaml (both image tag and label)
sed -i "" "s/image: weshigbee\/examples-super-orders:$CURRENT_VERSION/image: weshigbee\/examples-super-orders:$NEW_VERSION/" compose.yaml
sed -i "" "s/app.version=$CURRENT_VERSION/app.version=$NEW_VERSION/" compose.yaml

# Update version in html template
sed -i "" "s/class=\"version-badge\">v$CURRENT_VERSION/class=\"version-badge\">v$NEW_VERSION/" templates/home.html
sed -i "" "s/Build: v$CURRENT_VERSION/Build: v$NEW_VERSION/" templates/home.html

echo "Version bumped successfully. Changes to commit:"
git diff --stat

echo ""
echo "Next steps:"
echo "1. Review the changes with 'git diff'"
echo "2. Commit the changes with 'git commit -am \"Bump version to $NEW_VERSION\"'"
echo "3. Rebuild and redeploy the application with 'docker compose build && docker compose up -d'"
