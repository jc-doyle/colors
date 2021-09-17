#!/bin/zsh

dirs=(
  "xresources/.Xresources"
  "alacritty/alacritty.yml"
  "polybar/config" 
  "rofi/rofi.rasi" 
  "nvim/lua/colors/colors.lua"
  "zsh/fzfcolors.zsh"
  "zathura/zathurarc"
  "dunst/dunstrc"
  "sc-im/theme"
)

for i in ${dirs[*]}; do
  pybase16 inject -s $1 -f "../config/"$i
done

state=$(autorandr --current)

if [ "$state" = "docked" ]; then
  zsh ~/.config/polybar/polydocked.sh
else 
  zsh ~/.config/polybar/polymobile.sh
fi

notify-send "Colorscheme: $1"
