#/bin/bash
echo "Enter character:\n"
#read - scanf
read n1
if [[$n1 -eq 1]]
then 
python3 vars.py
fi 
if [[$n1 -eq 2]]
then
python3 string.py
fi
echo "Done:\n"

