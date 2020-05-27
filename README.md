# playfield
Field of play markers and 2-d overlays for live sports


## Setup and configuration
The library is designed to run on docker with GPU acceleration. Tests and timings
were run on a consumer grade homelab with the following specifications:

* Operating System: Ubuntu 18.04
* CPU: AMD Ryzen 3900x, 12 core
* GPU: Nvidia GeForce RTX 2070 Super (8gb)
* RAM: 64GB DDR4
* HDD: NVME SSD

## Docker setup
The docker commands are issued via a Makefile since GPU accelleration flags don't work
well via docker-compose, and the author doesn't remember all of the flags. For information
on the commands, run `make help`.


### ToDos
To be deprecated from the readme and added as issues once fleshed out

#### 30,000 ft. view
 1. Download and clean training data
 2. For the training data, identify the "field of play" (n.b., starting with 1 or 2 sports
 with well-defined boundaries)
 3. Identify player objects from the camera feed
 4. _Follow_ player objects
 5. Project player objects to the 2d field of play


 #### immediate next steps
  1. Static images for fields of play to build training set
    * mark "Corners" and project to a 2d overlay. By default, standard field sizes will apply
    * train a model to identify the corners for the projection

