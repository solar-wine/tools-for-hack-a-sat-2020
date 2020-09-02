# Ghidra server

We set up a [Ghidra server](https://ghidra-sre.org/) to facilitate collaborative reverse engineering.

## Running the server

This server is configured to have no authentication, do not expose it on the Internet.

To build the docker images and run them, use the following command:
```
docker-compose up -d
```


## Client configuration

* Ensure that you can reach the following TCP ports on the server:
  * 13100
  * 13101
  * 13102
* Select the `File` menu, then `New...`
* Use the following settings:
  * server = `127.0.0.1`
  * port = `13100` (default value)
  * username = anything is accepted
  * password = anything is accepted

* Ghidra will use your local user name by default. If you wish to use a different username on the remote machine, add this to your `${GHIDRA_HOME}/support/launch.properties`: `VMARGS=-Duser.name=my_chosen_remote_username`

