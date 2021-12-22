echo "commit.sh started"
cd $GITHUB_WORKSPACE
git config --global user.name "FunctionalMetatable"
git config --global user.email "FunctionalMetatable@users.noreply.github.com"
echo "[commit.sh]: committing locally"
git commit -m "[update-curators-action] Updating members" -a
echo "[commit.sh]: pushing to github"
git push
echo "completed commit.sh"
