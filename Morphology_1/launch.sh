#!/bin/bash
set -ex

# 8.2 build
# 8.2 buildclang
# temp build
# temp buildclang

source $HOME/neuron/prefixenv $1/$2/install
mkdir -p $1-$2
cd $1-$2
#nrnivmodl -incflags "-I/home/hines/soft/Caliper/build/install/include" ../mod_files
nrnivmodl ../mod_files

export PYTHONPATH=`pwd`/..:$PYTHONPATH
#CALI_CONFIG=runtime-report,calc.inclusive nrniv -c 'mycpu=1' -c 'chdir("..")' protocols/01_SS.py

#perf record nrniv -c 'mycpu=8' -c 'chdir("..")' protocols/01_SS.py
#nrniv -c 'mycpu=4' -c 'chdir("..")' protocols/01_SS.py
perf stat nrniv -c 'mycpu=8' -c 'chdir("..")' protocols/01_SS.py

if false ; then
$ cmake .. -G Ninja -DCMAKE_INSTALL_PREFIX=install \
  -DPYTHON_EXECUTABLE=`pyenv which python` -DNRN_ENABLE_RX3D=OFF \
  -DNRN_ENABLE_PROFILING=ON -DNRN_PROFILER=caliper \
  -DCMAKE_PREFIX_PATH=$HOME/soft/Caliper/build/install/share/cmake/caliper
fi
