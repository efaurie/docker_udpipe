# UDPipe Docker Container
This repository contains a docker container which runs a RESTful HTTP interface for UDPipe, a Universal Dependency based parser.

## Build
Build the container with the build.sh bash script.

## Run
Run the container forwarding some local `<PORT>` to container port 8080.

`docker run -p <PORT>:8080 udpipe`

## Use
Submit HTTP `GET` requests to the server using the endpoint `http:<HOST>:<PORT>/process`, and follow the API definition found [here](http://lindat.mff.cuni.cz/services/udpipe/api-reference.php).



