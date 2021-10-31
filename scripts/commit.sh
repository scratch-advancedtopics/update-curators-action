echo "commit.sh started"
cd $GITHUB_WORKSPACE
git config --user.name "ScratchATs-bot[bot]"
git config --user.email "ScratchATs-bot[bot]@users.noreply.github.com"
echo "[commit.sh]: committing locally"
git commit -m -a "update members"
echo "[commit.sh]: pushing to github"
git push
echo "completed commit.sh"
