# SAVO js game

## Client
Best practice would be to host the subfolders lib and media of impact with nginx.
And proxy forward / to node. Weltmeister is nice for development, but is php.

## Backend API
Add a folder named secret and a subfolder, jwt-keys. You need RSA keys in key.pem and key.pub.
You may also add a admin.txt in the secret folder for adding an admin account.

## Running
Just the typical node application, with a python backend and mongo as the database.
Easiest way of runnig is by docker-compose.

### Deug
```
docker-compose -f dev-compose.yml up
```

# TODO:
- non-nginx dev env? nignx seems to hide some api errors and would be nice to try weltmeister.
- make actual game
- make cool client
- bake.sh
