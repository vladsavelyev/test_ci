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

# Building the conda package
RUN conda create -n hailenv hail google-cloud-sdk google-cloud-storage

COPY hail-deploy-config.json /

ENV PATH /miniconda/envs/hailenv/bin:$PATH
