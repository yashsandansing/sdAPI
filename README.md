# sdAPI
Repo for stable diffusion API's assignment. 

The pytorch libraries are installed for CPU since my system didn't have enough VRAM to accomodate the large models of "bark".

Models from the "bark" repo are installed at the time of building the docker container. (A poor network connection might interrupt the build due to bark's s3 issues).

Return type is an audio file(.wav) that you can download.
