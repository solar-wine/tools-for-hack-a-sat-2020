#!/bin/bash
while true; do
  cd /install/idarling
  python3 -c 'import idarling.server; idarling.server.main()' --no-ssl -l DEBUG -h 0.0.0.0
done
