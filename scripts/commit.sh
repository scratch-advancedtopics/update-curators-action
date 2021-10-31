echo "commit.sh started"
cd $GITHUB_WORKSPACE
git config --local user.name "ScratchATs-bot[bot]"
git config --local user.email "ScratchATs-bot[bot]@users.noreply.github.com"
echo "[commit.sh]: committing locally"
git commit -m "update members" -a
echo "[commit.sh]: pushing to github"
git push
echo "completed commit.sh"
