FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y locales curl gnupg lsb-release software-properties-common \
    && locale-gen en_US en_US.UTF-8 && add-apt-repository universe
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu jammy main" > /etc/apt/sources.list.d/ros2.list
RUN apt-get update && apt-get install -y ros-humble-ros-base python3-colcon-common-extensions
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
WORKDIR /repo
