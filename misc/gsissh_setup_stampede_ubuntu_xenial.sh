#!/bin/sh

touch /etc/apt/sources.list.d/globus-toolkit-6-stable-xenial.list

## Installing "globus-proxy-utils" "globus-simple-ca"
sudo echo "deb http://toolkit.globus.org/ftppub/gt6/stable/deb xenial contrib" >> /etc/apt/sources.list.d/globus-toolkit-6-stable-xenial.list
sudo echo "deb-src http://toolkit.globus.org/ftppub/gt6/stable/deb xenial contrib" >> /etc/apt/sources.list.d/globus-toolkit-6-stable-xenial.list
sudo apt-get update
sudo apt-get install globus-proxy-utils globus-simple-ca

## Installing "ca-policy-egi-core" - 1
cd
mkdir tmp
cd tmp
wget http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo%5flatest%5fall.deb
dpkg -i globus-toolkit-repo_latest_all.deb
sudo apt-get update
sudo apt-get install ca-policy-egi-core


## Installing "ca-policy-egi-core" - 2
#curl https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3 | sudo apt-key add -
#sudo echo "deb http://repository.egi.eu/sw/production/cas/1/current egi-igtf core" >> /etc/apt/sources.list
#sudo apt-get update
#sudo apt-get install ca-policy-egi-core

# Remove local certificates - caution
#rm -r $HOME/.globus/certificates

# Setup myproxy, should prompt for password. If successful, run following commented command.
myproxy-logon -s myproxy.xsede.org -l vivek91
#gsissh -p 2222 vivek91@stampede.tacc.xsede.org


# If gsissh is not found install gsi-openssh-clients
