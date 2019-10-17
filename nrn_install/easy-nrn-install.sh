#Tyler Banks
#Grab MPI Neuron and IV, install
#Instructions from https://www.neuron.yale.edu/neuron/download/getstd
#http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1-installguide.pdf
#https://www.neuron.yale.edu/phpBB/viewtopic.php?t=3062

if [ -z $1 ]; then
        echo "Directory to install not specified, exiting."
        exit 0
else
        echo "Installing Neuron into $1/nrn"
fi


#cmd line arg $1
touch $1/nrnenv
mkdir $1/nrn
echo "export NRN_INSTALL_DIR=$1/nrn" >> $1/nrnenv
echo 'export NRN_DIR=$NRN_INSTALL_DIR/neuron_install' >> $1/nrnenv
source $1/nrnenv

mkdir $NRN_DIR
cd $NRN_DIR
wget https://neuron.yale.edu/ftp/neuron/versions/v7.7/nrn-7.7.tar.gz
tar xzf nrn-7.7.tar.gz
# renaming the new directories iv and nrn makes life simpler later on
mv nrn-7.7 nrn

#Install IV

cd nrn
./configure --prefix=`pwd` --without-iv --with-nrnpython=`which python`
make
make install

cd neuron_install/nrn/src/nrnpython/
python setup.py install

#Make it easy to use

echo 'export N=$NRN_DIR/nrn' >> $1/nrnenv
echo 'export CPU=x86_64' >> $1/nrnenv
echo 'export PATH="$N/$CPU/bin:$PATH"' >> $1/nrnenv

source $1/nrnenv
echo "source $1/nrnenv" >> $HOME/.bashrc
