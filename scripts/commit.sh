echo "commit.sh started"
cd $GITHUB_WORKSPACE
git config --global user.name "ScratchATs-bot[bot]"
git config --global user.email "ScratchATs-bot[bot]@users.noreply.github.com"
echo "[commit.sh]: committing locally"
git commit -m "update members" -a
echo "[commit.sh]: pushing to github"
git push
echo "completed commit.sh"
