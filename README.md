The application runs on a docker engine. It was tested using Ubuntu 20.04.

## System requirements
```bash
$ sudo apt install curl
$ sudo apt install git
```
### Installing crane
```bash
bash -c "`curl -sL https://raw.githubusercontent.com/michaelsauter/crane/v2.11.0/download.sh`" && chmod +x crane && sudo mv crane /usr/local/bin/crane
```
### Installing docker
Depending on your distributions follow the steps in the official documentation.

For Ubuntu: https://docs.docker.com/engine/install/ubuntu/
```bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
$ echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
### Configuring docker
```bash
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```

### Getting the source code
```bash
$ git clone git@github.com:enzocc/marketplace.git
```

## Running the application
```bash
cd ~/marketplace
crane lift
```

## Seeding the database
Execute the following commands:

```bash
curl -X POST --header 'Accept: application/json' '127.0.0.1:5000/product' -d '{"name":"Lavender heart", "price": 9.25}'
curl -X POST --header 'Accept: application/json' '127.0.0.1:5000/product' -d '{"name":"Personalised cufflinks", "price": 45.00}'
curl -X POST --header 'Accept: application/json' '127.0.0.1:5000/product' -d '{"name":"Kids T-shirt", "price": 19.95}'
```

After this, the data base will contain:

| Product code  | Name  |  Price |
|---|---|---|
|  001 |  Lavender heart | £9.25  |
|  002 |  Personalised cufflinks | £45.00  |
|  003 |  Kids T-shirt | £19.95 |

## Testing the application
### Manual Testing
The application was tested using the curl commands:
```bash
$ curl -X POST --header 'Accept: application/json' '127.0.0.1:5000/product' -d '{"name":"PRODUCT_NAME", "price": PRODUCT_PRICE}'
$ curl -X GET --header 'Accept: application/json' '127.0.0.1:5000/products'
$ curl -X GET --header 'Accept: application/json' '127.0.0.1:5000/product/{product_id}'
$ curl -X PUT --header 'Accept: application/json' '127.0.0.1:5000/product/{product_id}' -d '{"price": NEW_PRICE, "name": "NEW_NAME"}'
$ curl -X DELETE --header 'Accept: application/json' '127.0.0.1:5000/product/{product_id}
```


### Automatic Testing
The tests can be found on `marketplace/api/app/tests`

Run them by executing:
``` bash
cd ~/marketplace/api/app/tests
pytest
```
