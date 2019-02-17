if [ -n "$TRAVIS_TAG" ]; then # only run conda-build on tags, takes too long
    # Install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh -q
    bash miniconda.sh -b -p $HOME/miniconda
    export PATH="$HOME/miniconda/bin:$PATH"
    conda config --set always_yes yes --set changeps1 no
    conda install conda-build anaconda-client
    conda update -q conda-build
    #conda info -a

    # Build conda packages (no wheels with conda on Linux)
    export ARTIFACTS_FOLDER=`readlink -f ./artifacts`
    cd dss_python
    conda-build --quiet --no-test --output-folder "$ARTIFACTS_FOLDER" conda 

    # Upload artifacts to anaconda.org
    if [ -n "$ANACONDA_API_TOKEN" ]; then 
        find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} anaconda upload --no-progress -l main -u pmeira {}
    fi
fi
