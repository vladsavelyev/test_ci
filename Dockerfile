# Inheriting from a service image that has conda and hail installed
FROM australia-southeast1-docker.pkg.dev/vlad-dev/test-ci/hailbatch:latest
MAINTAINER Centre for Population Genomics "https://github.com/populationgenomics"

RUN mkdir -p /work
WORKDIR /work
COPY setup.py requirements.txt /work/
COPY scripts /work/scripts
COPY test_ci /work/test_ci
COPY test /work/test
COPY conda /work/conda
COPY README.md /work/README.md

RUN conda install conda-build conda-verify anaconda-client
RUN conda build conda/test_ci
RUN conda create --use-local -n env test_ci
ENV PATH /miniconda/envs/env/bin:$PATH

RUN wget https://broad.io/install-gcs-connector

# Clean up
RUN rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    cd /usr/local && \
    apt-get clean && \
    rm -rf /.cpanm
