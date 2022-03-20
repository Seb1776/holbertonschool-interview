$direc=$args[0]
$comm=$args[1]
git add $direc
git commit -m $comm
git push origin main