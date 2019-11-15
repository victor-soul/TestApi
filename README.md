## README.md

#### Starting application:
1. Download and install `docker`
2. Download and install `docker-compose` - after this step maybe necessary to reboot you machine
3. Generate your token on genius api 
4. Put in your envars or open `docker-compose.yml` and replace the `TOKEN` value under `services->api->environment`  *only necessary if you whant to run tests*
4. `make build`
5. `make up`

#### Making requests
*use postman or whatever tool you may like*

1. Add the `TOKEN` on your Authorization Header - `Bearer`
2. Url `http://0.0.0.0:8080/search?query={Artist Name}`

#### Caviats
* to run the tests `make tests`
* to see `stdout` from the container `make logs`
