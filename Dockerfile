FROM ubuntu:18.04
MAINTAINER Centre for Population Genomics "https://github.com/populationgenomics"

RUN apt-get update && \
    apt-get install -y curl wget git unzip tar gzip bzip2 g++ make \
        zlib1g-dev nano openjdk-8-jre-headless

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh \
    --no-verbose -O miniconda.sh && \
    chmod +x miniconda.sh && \
    bash miniconda.sh -b -p /miniconda && \
    rm miniconda.sh
ENV PATH /miniconda/bin:$PATH
RUN conda config --set always_yes yes --set changeps1 no && \
    conda config --add channels bioconda --add channels conda-forge --add channels cpg
RUN conda install pip conda-build anaconda-client conda-verify

RUN mkdir -p /work
WORKDIR /work
COPY setup.py requirements.txt /work/
COPY scripts /work/scripts
COPY test_ci /work/test_ci
COPY test /work/test
COPY conda /work/conda
COPY README.md /work/README.md

# Building the conda package
RUN conda build conda/test_ci
RUN conda create --use-local -n testenv "python==3.7.*" test_ci
ENV PATH /miniconda/envs/testenv/bin:$PATH

# Getting the connector
RUN wget https://broad.io/install-gcs-connector

# Clean up
RUN rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    cd /usr/local && \
    apt-get clean && \
    rm -rf /.cpanm
