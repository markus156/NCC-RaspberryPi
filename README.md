# NCC-RaspberryPi
-------------------
## Idea
For our clusterprojekt we want to have a server, which controls the whole cluster.

The server should manager the following things:
* It should reboot and restart the clients
* New Clients get registered in the database and get removed, if they disconnect
* The server distributed MPI-jobs, so we can choose, which clients are working on which project/job/problem

-------------------

## Current status
* The server can accept data and displays the data
* The server logs the clients, which are connected to the server, later this list will be stored in our database and will be displayed on the website
