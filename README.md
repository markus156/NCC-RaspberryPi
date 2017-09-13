# NCC-RaspberryPi
===========================================================================================================
##Idea
For our clusterprojekt we want to have a server, which controlls the whole cluster.

The server should manager the following things:
* Shutdown and reboot clientnodes
* New Clients get regitered in the database and get removed, if they disconnect
* The server distributed MPI-jobs, so we can choose, chich clients are working on which projekt/job/problem

-------------------------------------------------------------------------------------------------------------

##Current status
* The server can accept data and displays the data
* The server loggs the clients, which are connected to the server, later this list will be stored in our database and will be displayed on the webside