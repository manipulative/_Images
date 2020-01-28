time=`date "+%Y-%m-%d_%H-%M-%S"`
git add --all
git commit -m "${time}"
git push origin master
echo "Finished Push"