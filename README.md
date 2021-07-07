# translator python 
this app is translate the last copy in your clipboard the default language that translate to is persian but you can change it.  
## requirement
- googletrans=4.0.0-rc1
- xclip 
- sxhkd
- python = +3.6

## Installation
    ```
    pip3 install googletrans==4.0.0-rc1
    
    # xclip arch-base
    sudo pacman -S xclip

    ```

Installation of xclip and sxhkd depends on your distro package manager

## using sxhkd to set a shortcut for app

    ```
    mkdir ~/.config/sxhkd
    cd ~/.config/sxhkd
    touch sxhkdrc
    echo -e "super + shift + t \n   python ./path_to_translator" >> sxhkdrc
    ```

and you most put sxhkd on startup app to shortcut run!!!
