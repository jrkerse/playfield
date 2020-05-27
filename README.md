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
