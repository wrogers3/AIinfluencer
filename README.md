# Welcome to Ai-influencer!

This repository is a project to utilise the latest stable diffusion capabilities of the open source developer realm.
(https://github.com/lllyasviel/Fooocus). 

# Goal
For every AI influencer face image, use that image to make 10 more pictures of her with a randomised prompt. 
The pictures are stored in a folder (Fooocus/output)
Human filters out the bad pictures
Script posts the remaining pictures to instagram (post.py)
Do that with 20 accounts, and then 100, expand!!!


# Files

There are 2 main functionalities of the files in this repository:

 - image generation (prompts, API script, API secrets..)
 - posting these pictures onto Instagram (using the instabot api)


## Requirements
WSL2 with CUDA compatibility (run nvidia-smi to check it). 


## Steps

Go to https://github.com/lllyasviel/Fooocus and follow their download instructions, after forming the python venv, run `python3 entry_with_update.py` to start the server. Then run  `python3 tester.py` to send information to the server.

## Docker Image

DOCKER IMAGE IS COMING SOON.

## Progress Update
The API of Fooocus is badly documented, and the tester.py would most likely need to be updated as Fooocus' API updates to a better interface.



manual pipeline for generating pics
parameters:
    image = 15
    resolution = 1152*896 | 9:7
    Performance = Quality
    Styles: Fooocus V2, Enhance, Sharp, Photograph
    Image Prompt+ Advanced = baseModelPic, stopat 0.9, weight = 1.650, FaceSwap
    Model = defaults

