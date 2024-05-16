# Spotify Example
This repo is for an example of data extraction project from Spotift

> **__NOTE__**: This repo is a new project still starting

## Requirements

- `Terraform`: In order to have fully access to Spotify we need some User Authorization and to do that we need to create some where to store the secrets that's why we need those secret store in the cloud
- `python`: This repo was build running python `3.12.2` you can set up your own enviroment with `conda`
- `Python Requirements`: 
    - Boto3: accessing AWS Resources
    - cherrypy: Lightweight Rest API for getting the authorization codes

## Authorization

Authorization in the Spotify is simple:

1. First login in to the desire account in the Spotify Developer [Website](https://developer.spotify.com/)
2. Create a new App on the [Dashboard](https://developer.spotify.com/dashboard) page
3. Check which method of authorization on the API is better for your needs, in this case we are using [Authorization Code Flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) as they are the [authorization](https://developer.spotify.com/documentation/web-api/concepts/authorization) method recommend for apps running on a `back-end`.
4. For the Client Crenditials we will need the `Client ID` and the `Client Secret`, this can be found in the dashboard -> {your awesome_app} -> settings
5. We will need to get the authorization code in order to use our own data personal data from spotify and do some interesting things


## Manual Steps Before Automating

1. Add the `client_credentials` to your secret in plain text like this

        {"client_id": "<client_id>","client_secret": "<client_secret>"}

2. Get the python requirements

        pip install requirement.txt

3. Startup the lightweight rest

        python local_rest/rest.py

> **__NOTE__**: This will start a small server

4. Go into this [url](http://0.0.0.0:8080/login) and authorized the request

5. Check in your AWS Console for all the secrets, they should be available now