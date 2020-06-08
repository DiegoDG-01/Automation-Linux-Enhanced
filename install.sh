# Inicialition
clear

ASCII=(' _       __________    __________  __  _________'
       '| |     / / ____/ /   / ____/ __ \/  |/  / ____/'
       '| | /| / / __/ / /   / /   / / / / /|_/ / __/   '
       '| |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___ '
       '|__/|__/_____/_____/\____/\____/_/  /_/_____/'
)

for i in "${ASCII[@]}"; do echo -e '\E[35m'"$i"; done

User=$(whoami)
OS=$(uname -s)
Rev=$(uname -r)
PM=$(apt -v || pacman -V)

echo -e '\n\t    \E[35m'"ALE script installer\n"
echo -e '\E[32m'"Operating System Type :" $OS
echo -e '\E[32m'"Operating System Version :" $Rev
echo -e '\E[32m'"Package Manager :" $PM

if [[ "$PM" == *"apt"* || "$PM" == *"pacman"* ]]; then

       echo -e '\n\E[33m'"Your system is supported, are you sure to installed? [Y=yes, N=no]" 
       read result       

       if [[ "${result}" == "Y" || "${result}" == "y" ]]; then

              if [[ "$PM" == "apt"* ]]; then
                     PM="APT"
              elif [[ "$PM" == "pacman"* ]]; then
                     PM="PACMAN"
              fi

              $(cp -r ../Automation-Linux-Enhanced ~/)
              $(cp ~/.bashrc ~/.bashrc.bak)
                            
              if [ -f ~/.bashrc.bak ]; then
                     echo -e '\n\E[32m'"Modifying essential files . . ."
                     RS=$(python3 ~/Automation-Linux-Enhanced/Temp/modify.py $PM $User)

                     if [[ "${RS}" == "True" ]]; then

                            echo -e '\E[32m'"Creating alias in .bashrc . . ."
                            echo "alias ale='python3 ~/Automation-Linux-Enhanced/ALE.py'" >> ~/.bashrc
                            $(source ~/.bashrc)
                     else
                            echo -e '\n\E[31m'"Error to modifying essential files" 
                     fi                                 
              else
                     echo -e '\n\E[31m'"Error to create backup the .bashrc"
              fi

              echo -e '\n\E[32m'"Installation Complete"

              echo -e '\n\E[33m'"Delete temporal files? [Y=yes, N=no]" 
              read result

              if [[ "${result}" == "Y" || "${result}" == "y" ]]; then
                     $(rm -rf ~/Automation-Linux-Enhanced/Temp)
              fi
              
              echo -e '\n\E[32m'"Installation Complete"

       elif [[ "${result}" == "N" || "${result}" == "n" ]]; then
              echo -e '\n\E[31m'"Installation canceled"
       else
              echo -e '\n\E[31m'"Invalid option"
       fi
else
       echo -e '\n\E[31m'"ERROR"
fi;

sleep 1