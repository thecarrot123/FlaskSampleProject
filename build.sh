#!/bin/bash
set -e

green="\e[32m"
red="\e[31m"
black="\e[0m"
blue="\e[94m"


create_init() {
    cd $1
    [ -f __init__.py ] && rm __init__.py
    files=$(ls | grep -E "*\.py")
    touch '__init__.py'
    for file in $files; do
        echo -e "${red}- ${black}Importing $file to $1"
        echo "from main.$1.${file::-3} import *" | tee -a __init__.py >> /dev/null
    done
    cd ..
    echo -e "${green}+ ${black}done!\n"
}

create_init_for_dir() {
    if [ -d $1 ]
    then
        echo -e "${blue}*${black} creating __init__.py for $1"
        create_init $1
        folders+=("$1")
    fi
}

[ ! -d main ] && echo "<main> directory not found." && exit
cd main
create_init_for_dir routes
create_init_for_dir models
create_init_for_dir forms
echo -e "created __init__.py files for: ${blue}${folders[@]}${black}"