# translator python 
this app is translate the last copy in your clipboard the default langauge that translate to is persian but you can change it.  
## requirment 
- googletrans=4.0.0-rc1
- xclip 
- sxhkd
- python = +3.6
### installion
    ```
    pip3 install googletrans==4.0.0-rc1
    
    # xclip arch-base
    sudo pacman -S xclip

    ```

    installion of xclip and sxhkd is depend on your distro package manager

## using sxhkd to set a shortcut for app
    ```
    mkdir ~/.config/sxhkd
    cd ~/.config/sxhkd
    touch sxhkdrc
    echo -e "super + shift + t \n   python ./path_to_translator" >> sxhkdrc
    ```
    and you most put sxhkd on startup app to shortcut run!!!
