FROM node:slim

MAINTAINER alaxallves@gmail.com

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install -y nodejs tree libfontconfig bzip2 xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 && npm install --quiet --global vue-cli

RUN mkdir /TropicalHazards-BI

COPY . /TropicalHazards-BI

WORKDIR /TropicalHazards-BI

# If you have any symblinks in your PC attached to the root folder and you DONT want them copied to your container, use COPY instead of ADD
ADD package.json /TropicalHazards-BI/package.json

RUN npm install
