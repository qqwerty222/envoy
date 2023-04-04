# Deploy services with envoy

There is 3 services in this project:
- MySQL database
- website (python flask)
- API (python flask)

## How to deploy

To deploy this project use: 
```bash
docker compose up -d
```

Output:
```bash
[+] Running 7/7
 ✔ Network envoy_website-net  Created                                                                                  0.1s
 ✔ Container envoy-api-2      Started                                                                                  1.5s
 ✔ Container envoy-db-1       Started                                                                                  1.1s
 ✔ Container envoy            Started                                                                                  0.9s
 ✔ Container envoy-api-1      Started                                                                                  0.9s
 ✔ Container envoy-website-1  Started                                                                                  1.2s
 ✔ Container envoy-website-2  Started                                                                                  1.9s
```

After you will see 7 containers
```bash
CONTAINER ID   IMAGE                            CREATED         STATUS         PORTS                NAMES
42c9576f0940   envoyproxy/envoy:v1.25-latest    5 seconds ago   Up 3 seconds   80/tcp, 9901/tcp     envoy
9229faf5b99e   envoy-api                        5 seconds ago   Up 2 second                         envoy-api-1
9acdc5747d5a   envoy-api                        5 seconds ago   Up 3 seconds                        envoy-api-2
e548e4c8c040   envoy-website                    5 seconds ago   Up 2 seconds                        envoy-website-1
1091641eab96   envoy-website                    5 seconds ago   Up 3 seconds                        envoy-website-2
f0f6a9ca61ea   mysql:latest                     5 seconds ago   Up 3 seconds   3306/tcp             envoy-db-1
```

- envoy  
    container with envoy proxy that expose ports 9901 for admin endpoint and 80 for ordinary http connections.  
- envoy-api-1/2  
    containers for api (source dir ./api)
- envoy-website-1/2  
    containers for website (source dir ./website)
- envoy-db-1  
    container with mysql database. Store data for api and website.  
    Run sql script from ./init_mysql in the end of initialization process.

## Config description

! after compose wait ~10 seconds, mysql container need time before it will be ready for connections.  

Envoy listen port 80, on localhost. It send request to api or website depended on url, "/" for website, "/api" for api. Also envoy distribute requests between different containers of 1 service. In docker compose deploy endpoint_mode is dnsrr. It means that docker service name returns a list of IP addresses (DNS round-robin), and the client connects directly to one of these. [(docs)](https://docs.docker.com/compose/compose-file/deploy/#endpoint_mode)

To prove it you can use dig from envoy container
```bash
root@envoy:/# dig website
...
;; ANSWER SECTION:
website.                600     IN      A       172.25.0.4
website.                600     IN      A       172.25.0.7
...
```
As you can see envoy get 2 ip addresses from docker dns 

## How to use
Available API endpoints:
```bash
curl localhost/api/status

curl localhost/api/company/

curl localhost/api/team/
curl localhost/api/team/lemon
curl localhost/api/team/lemon/size
curl localhost/api/team/lemon/tasks

curl localhost/api/worker/
curl localhost/api/worker/1
curl localhost/api/worker/1/team
curl localhost/api/worker/1/tasks
``` 

Website have only 1 index page with couple of tables filled from mysql db:
```bash
curl localhost/
```

Also you can see logs of api using:
```bash
docker logs envoy-api-1
docker logs envoy-api-2
```

Or with -f to attach stdout
```bash
docker logs -f envoy-api-1
docker logs -f envoy-api-2
```