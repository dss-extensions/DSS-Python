if [ "$DSS_PYTHON_BUILD_TAG" == "1" ]; then
    if [ -n "$ANACONDA_API_TOKEN" ]; then 
        echo Upload artifacts to anaconda.org...
        find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} anaconda upload --no-progress -l main -u pmeira {}
    fi
fi

# Always upload to AppVeyor
find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} appveyor PushArtifact {}