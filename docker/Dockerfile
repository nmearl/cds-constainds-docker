ARG BASE_REPO=jupyterhub/singleuser

FROM $BASE_REPO


USER root

SHELL ["/bin/bash", "--login", "-c"]

# Need to get gcc in the linux environment
RUN apt update \ 
    && apt install -y gcc \
    && apt install -y gfortran \
    && apt install -y curl \
    && apt install -y libxml2-dev libxslt-dev \
    && apt-get remove -y nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs

# For pinned verions of older voila, we need an older version of nodejs
# RUN apt-get remove -y nodejs
# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs
# SHELL ["/bin/bash", "--login", "-i", "-c"]
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# RUN source /root/.bashrc && nvm install 16
# SHELL ["/bin/bash", "--login", "-c"]


USER $NB_UID

RUN conda create -n default python=3.8 --quiet --yes
# RUN echo "conda activate default" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

# ARG conda_env=default
ENV PATH /opt/conda/envs/default/bin:$PATH
ENV CONDA_DEFAULT_ENV default
SHELL ["conda", "run", "-n", "default", "/bin/bash", "-c"]

# Install cosmicds + hubbleds
# RUN /bin/bash -c conda activate default \ 
#     && conda install --quiet --yes -c conda-forge git numpy "scipy>=1.1" cython lxml astropy pandas matplotlib scikit-image h5py \
#     && pip install 'jhsingle-native-proxy>=0.7.6' git+https://github.com/nmearl/hubbleds.git
# RUN conda install --quiet --yes "python<3.9" \
RUN conda install --quiet --yes -c conda-forge git numpy "scipy>=1.1" cython lxml astropy pandas matplotlib scikit-image h5py \
    && pip install 'jhsingle-native-proxy>=0.7.6' git+https://github.com/nmearl/hubbleds.git

RUN rm -rf /home/jovyan/work


COPY jupyter_notebook_config_extra.py /etc/jupyter/
RUN cat /etc/jupyter/jupyter_notebook_config_extra.py >> /etc/jupyter/jupyter_notebook_config.py
RUN rm /etc/jupyter/jupyter_notebook_config_extra.py

COPY voila.json /etc/jupyter

# Enable local conda envs
RUN conda init bash

# Fix permissions on /etc/jupyter as root
USER root
RUN fix-permissions /etc/jupyter/

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID