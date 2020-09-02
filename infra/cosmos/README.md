# Cosmos graphical interface

This set of containers runs the COSMOS graphical interface as provided by the
organizers, using [xpra](https://xpra.org/) as an X server. This effectively
acts as a `screen` for X applications, allowing team members to connect to the
graphical interface running on the machine that is attached to the flatsat.

This was mainly used during the preparation phase, before the final event of
the competition.

## Running the server

To build the docker images and run them, use the following command:
```
docker-compose up -d
```

## Connecting to the server

To connect to the server running this application, use SSH with port forwarding:

```
ssh -L6010:127.0.0.1:6010 user@server
```

Then, on their local machine, team members used the following command:

```
xpra attach tcp://localhost:6010/
```

