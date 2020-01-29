cd /Users/siyuan/OneDrive/function/_Images

read -p "please input .md dictionary:" dictionary
python3 /Users/siyuan/OneDrive/function/_Images/_replace.py $dictionary

time=`date "+%Y-%m-%d_%H-%M-%S"`
git add --all
git commit -m "${time}"
git push origin master
echo "Finished Push"