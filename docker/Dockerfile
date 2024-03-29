# docker buildx build --platform linux/amd64,linux/arm64 -t nmearl/cds-jsp:0.1.2 --push . --no-cache
ARG BASE_REPO=jupyterhub/singleuser

FROM $BASE_REPO


USER root

SHELL ["/bin/bash", "--login", "-c"]

# Need to get gcc in the linux environment
RUN apt update \ 
    && apt install -y \ 
        gcc \
        g++ \
        gfortran \
        cmake \
        curl \
        libxml2-dev \
        libxslt-dev \
        software-properties-common \
        npm \
    # && npm install npm@latest -g \
    # && npm install n -g \
    # && n latest \
    # && apt-get remove -y nodejs \
    && rm -rf /var/lib/apt/lists/*
    # && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    # && apt-get install -y nodejs

# For pinned verions of older voila, we need an older version of nodejs
# RUN apt-get remove -y nodejs
# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs
# SHELL ["/bin/bash", "--login", "-i", "-c"]
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# RUN source /root/.bashrc && nvm install 16
# SHELL ["/bin/bash", "--login", "-c"]


USER $NB_UID


# COPY environment.yaml /home/jovyan/
# RUN conda env create --file environment.yaml

# RUN conda create -n default python=3.8 --quiet --yes
# RUN echo "conda activate default" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

ENV NODE_OPTIONS --openssl-legacy-provider
# ARG conda_env=default
# ENV PATH /opt/conda/envs/default/bin:$PATH
# ENV CONDA_DEFAULT_ENV default
RUN conda install python=3.8 --quiet --yes
# SHELL ["conda", "run", "-n", "default", "/bin/bash", "-c"]

# Install cosmicds + hubbleds
RUN conda install --quiet --yes -c conda-forge git
RUN conda install --quiet --yes -c conda-forge numpy
RUN conda install --quiet --yes -c conda-forge "scipy>=1.1"
RUN conda install --quiet --yes -c conda-forge cython 
RUN conda install --quiet --yes -c conda-forge lxml
RUN conda install --quiet --yes -c conda-forge astropy
RUN conda install --quiet --yes -c conda-forge pandas
# RUN conda install --quiet --yes -c conda-forge matplotlib
RUN conda install --quiet --yes -c conda-forge scikit-image
RUN conda install --quiet --yes -c conda-forge h5py
RUN conda install --quiet --yes -c conda-forge openblas
RUN pip install --upgrade pip
RUN pip install "jupyter-server-proxy==3.2.2" "aiohttp==3.8.4" 
RUN pip install git+https://github.com/nmearl/hubbleds.git

# Enable local conda envs
RUN conda init bash
# RUN jupyter labextension install @jupyterlab/server-proxy
# RUN jupyter serverextension enable --sys-prefix jupyter_server_proxy

RUN rm -rf /home/jovyan/work

COPY jupyter_server_config_extra.py /etc/jupyter/
RUN cat /etc/jupyter/jupyter_server_config_extra.py >> /etc/jupyter/jupyter_server_config.py
RUN rm /etc/jupyter/jupyter_server_config_extra.py

COPY jupyter_config.json /etc/jupyter


# Fix permissions on /etc/jupyter as root
USER root
RUN fix-permissions /etc/jupyter/

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID