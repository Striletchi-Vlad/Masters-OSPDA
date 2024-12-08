FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    slurm-wlm munge openssh-server openssh-client \
    libpmi1-pmix libpmi2-pmix libpmix-dev libpmix2 libopenmpi-dev libopenmpi3 libpmi-pmix-dev && \
    rm -rf /var/lib/apt/lists/*

# Setup SSH
RUN mkdir /var/run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN apt-get update && apt-get install -y \
    openmpi-bin libopenmpi-dev && \
    rm -rf /var/lib/apt/lists/*

# Setup user and munge
# RUN useradd -m slurm && \
RUN \
    mkdir -p /etc/munge /var/log/slurm /var/spool/slurmd && \
    chown -R slurm: /var/log/slurm /var/spool/slurmd

RUN mkdir -p /var/spool/slurm && \
    touch /var/spool/job_state /var/spool/job_state.old && \
    chown -R slurm: /var/spool && \
    chmod 0700 /var/spool

RUN mkdir -p /var/log/munge && \
    chown munge:munge /var/log/munge && \
    chmod 0700 /var/log/munge

RUN mkdir -p /etc/munge /var/log/munge /run/munge && \
    chown -R munge: /etc/munge /var/log/munge /run/munge && \
    chmod 0700 /etc/munge /var/log/munge /run/munge && \
    /usr/sbin/create-munge-key

EXPOSE 22

CMD ["/bin/bash", "-c", "service ssh start && munged --force && slurmd -D"]
