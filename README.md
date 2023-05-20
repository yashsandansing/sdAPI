# sdAPI
Implement an API that convert's your text to speech using the bark repository

The pytorch libraries are installed for CPU since my system didn't have enough VRAM to accomodate the large models of "bark" (If you have a GPU on your system (>4GB), skip the `requirements.txt` file's pytorch dependencies and download the pytorch according to your system's CUDA version from www.pytorch.org) 

Models from the "bark" repo are installed at the time of building the docker container. (A poor network connection might interrupt the build due to bark's s3 issues).

Return type is an audio file(.wav) that you can download.

To run, follow steps:

1. Install `docker` in your system.
2. Run `docker build https://github.com/yashsandansing/sdAPI`
3. After the build has been completed, run `docker run image-id`.

After building and running the project, your localhost will display a FastAPI screen.
Input your text and wait for a few minutes before getting your .wav file as an output.
