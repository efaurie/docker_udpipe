FROM alpine:3.7

RUN apk update
RUN apk add --update --no-cache alpine-sdk clang wget unzip

#get udpipe code
WORKDIR /udpipe
RUN wget -q https://github.com/ufal/udpipe/archive/master.zip && unzip -q master.zip && rm -f master.zip
WORKDIR /udpipe/udpipe-master/src

#make udpipe server
RUN make server

WORKDIR /udpipe/udpipe-master/src/rest_server

#add language models
ADD models/english-ud-1.2-160523.udpipe .

EXPOSE 8080

#start udpipe REST server
#add language models to be started with server
CMD ["./udpipe_server", "8080", "en", "en", "./english-ud-1.2-160523.udpipe", "English UniversalDependencies 1.2"]
