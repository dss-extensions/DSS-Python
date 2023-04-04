cd dss_python

if [ "$RUNNER_OS" = "Windows" ]; then
    CONDA=`cygpath "$CONDA"`
    export ARTIFACTS_FOLDER=`readlink -f ../artifacts`
fi

export PATH=$CONDA:$CONDA/bin:$CONDA/scripts:$PATH

source $CONDA/etc/profile.d/conda.sh

# Update the recipe
DSS_PYTHON_PREPARE_BOA=1 python setup.py

conda config --set always_yes yes --set changeps1 no
conda config --add channels conda-forge
conda create -p ../boa boa anaconda-client
conda activate boa

PYTHON_VERSIONS="3.7 3.8 3.9 3.10 3.11"
for pyversion in $PYTHON_VERSIONS
do
    # Workaround to build when a single version fails
    echo "python:" > conda/version.yaml
    echo "    - $pyversion" >> conda/version.yaml
    boa build --no-test conda -m conda/version.yaml
done

#boa build --no-test conda -m conda/conda_build_config.yaml

mv $CONDA/conda-bld/*-64 $ARTIFACTS_FOLDER/
