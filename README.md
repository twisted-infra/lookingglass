# Through The Looking-Glass, And What Twisted Found There

The third generation of Twisted infrastructure. Now with 100% more Docker!

## Building images

```
cd services
docker-compose build
```

## Setting up configuration

```
cd services
mkdir kenaansecret
```

In `kenaansecret/__init__.py` put:

```
# Hostname of the IRC server to which we will connect
IRC_SERVER = 'irc.freenode.net'
IRC_PORT = 6667

# Nickname to use on that IRC server
BOT_NICK = 'kenaan_test'

# Password for this nickname
BOT_PASS = ''
```

## Running

```
cd services
docker-compose up -d
```
