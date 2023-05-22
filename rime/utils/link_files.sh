#!/usr/bin/env bash

# get repo directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
DIR="${DIR%/*}"

# check os
os=$(uname -s)
case $os in
  Linux*)
    [ -d "$HOME/.config/fcitx/rime/" ] && TARGET_DIR="$HOME/.config/fcitx/rime"
    ;;
  Darwin*)
    TARGET_DIR="$HOME/Library/Rime/";;
esac

read -p "Target directory[$TARGET_DIR]: " target_dir_user

[ -n "$target_dir_user" ] || target_dir_user="$TARGET_DIR"

for i in "$DIR/*"
do
  ln -s $i $target_dir_user
done
