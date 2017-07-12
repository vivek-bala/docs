#!/bin/sh

## Installing "globus-proxy-utils" "globus-simple-ca"		
sudo echo "deb http://toolkit.globus.org/ftppub/gt6/stable/deb xenial contrib" >> /etc/apt/sources.list.d/globus-toolkit-6-stable-xenial.list		
sudo echo "deb-src http://toolkit.globus.org/ftppub/gt6/stable/deb xenial contrib" >> /etc/apt/sources.list.d/globus-toolkit-6-stable-xenial.list		
sudo apt-get update		
sudo apt-get install globus-proxy-utils globus-simple-ca

## Installing "ca-policy-egi-core" - 1
# cd
# mkdir tmp
# cd tmp
# wget http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo%5flatest%5fall.deb
# dpkg -i globus-toolkit-repo_latest_all.deb
# sudo apt-get update
# sudo apt-get install gsi-openssh-clients globus-data-management-client myproxy globus-proxy-utils globus-simple-ca ca-certificates ca-digicertassuredidrootca-root ca-digicertgridca-1-classic ca-digicertgridca-1g2-classic-2015 ca-digicertgridrootca-root ca-digicertgridtrustca-classic ca-digicertgridtrustcag2-classic globus-gsi-cert-utils-progs libglobus-gsi-cert-utils0 ssl-cert 

## Installing "ca-policy-egi-core" - 2
curl https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3 | sudo apt-key add -
cd /etc/apt/sources.list.d
sudo touch egi-igtf-core.list
sudo echo "deb http://repository.egi.eu/sw/production/cas/1/current egi-igtf core" >> egi-igtf-core.list
sudo apt-get update
sudo apt-get install ca-policy-egi-core

# Alternative distribution via eugridpma
# sudo touch igtf-accredited.list
# sudo echo "deb http://dist.eugridpma.info/distribution/igtf/current igtf accredited" >> igtf-accredited.list
# sudo apt-get update
# sudo apt-get install ca-*

# Remove local certificates - caution
#rm -r $HOME/.globus/certificates

# Setup myproxy, should prompt for password. If successful, run following commented command.
myproxy-logon -s myproxy.xsede.org -l vivek91
#gsissh -p 2222 vivek91@stampede.tacc.xsede.org

# If gsissh is not found install gsi-openssh-clients
