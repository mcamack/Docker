# Docker

## References

* https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/

## Flask Server

* The `docker build` or `docker-compose build` command runs the instructions found in the Dockerfile and generates a custom container. 
* The last `ENTRYPOINT` line executes when the container first starts. The startServer.sh script will be run as soon as the container starts.

## Postman

[![Image Alt Text](postman.png)](postman)  
Use Postman to test out the REST API

Send a simple array of values to the REST endpoint /numpy and see that it returns a numpy formatted value:
[![Image Alt Text](postman_result.png)](results)  
