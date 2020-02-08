#Obviously this only runs on CentOS or OS supporting yum installs
yum -y update
yum -y install yum-utils
yum install -y epel-release
yum -y groupinstall development
yum -y install acpid && systemctl start acpid && systemctl enable acpid
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u
yum -y install python36u-pip
yum -y install whois
yum -y install nikto 
pip3.6 install google-api-python-client
pip3.6 install mysql-connector
pip3.6 install piexif
pip3.6 install stem
pip3.6 install discord
pip3.6 install cython
pip3.6 install requests
pip3.6 install webscreenshots
pip3.6 install selenium
pip3.6 install Pillow
pip3.6 install gTTS
pip3.6 install whois
pip3.6 install pyAesCrypt
pip3.6 install traceroute
pip3.6 install Pastebin
pip3.6 install eventlet
pip3.6 install beautifulsoup4
pip3.6 install pytesseract
pip3.6 install pytube
yum-config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/CentOS_7/
sudo rpm --import https://build.opensuse.org/projects/home:Alexander_Pozdnyakov/public_key
yum -y install tesseract 
yum -y install tesseract-langpack-deu
yum -y install whois
yum -y install traceroute
yum -y install bind-utils
yum install -y screen
yum install -y nano
yum install -y dnf
dnf install -y glibc fontconfig
yum install -y lbzip2
yum install -y fontconfig
yum install -y freetype
yum install -y wget
yum install -y bzip2
