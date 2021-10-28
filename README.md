# Wiping your T-EARS with NAPKIN
NAPKIN is a fork/continuation of the SCANIA+RISE project SAGA https://github.com/scania/saga.git <br> Napkin is currently(always) under heavy development. 

## Running Napkin Without Back-End Servers:

    sudo apt-get update
    sudo apt-get upgrade --yes
    sudo apt-get install git --yes
    git clone https://danielFlemstrom@bitbucket.org/danielFlemstrom/napkin.git

Double click on the file: `~/napkin/dist/index.html`     

## Preparing the Development Environment Container
Note, you need to have Docker installed on your local machine. <br>
From now on we decided to use a dockerized development environment since it is quite a lot of work to get all dependencies to work. 
The dependencies are specificed in two places: in the `<napkin>/Docker/pyproject.toml` and `<napkin>/client/package.json`.<br>
<hr>
On you local machine, prepare a source directory (the example uses /Users/dfm01/Documents/aProjects/napkincontainer)

Start with checking out the source there: 

    git clone git@bitbucket.org:danielFlemstrom/napkin.git

Build the development environment Docker container:<br>
In the root of the git repository:

     docker build -f Docker/Dockerfile.development -t tdev .

## Running the Development Environent Container:
The container does not contain any project specific data, instead you share the napkin git repo you cloned to your local harddrive.<br>
In your local machine, start the container by:

    export MY_LOCAL_GIT_PROJECT=/Users/dfm01/Documents/aProjects/napkincontainer
    docker container run --interactive -p 8080:8080 -p 4001:4001 --mount type=bind,source=$MY_LOCAL_GIT_PROJECT,target=/home/ubuntu/proj  --tty --rm tdev bash

The commands mounts the source directory on your harddrive so it is accessible inside the container. Now you can use e.g. vscode to edit the files in your local machine, and the changes are visible to the container. 

Inside the container, you need to install the npm modules (once, since it writes them to your local harddrive):

    cd <napkin>/client
    npm install

A lot of warnings are issued because the versions are old. This should be fixed by someone...<br>


## Running The Development Server in the Development Environment Container
### Global project settings: 
    
    cp <napkin>/env_example .env

Adjust if necessary.
## Starting the development servers:
In <napkin>/client:<br>

    npm run dev



# Old stuff

For unknown reason, there is a npm_modules under 
`client/js/brace` as well. Probably only needed if you rebuild ace editor. A `npm install .`should do it if that is the case. 

 
        cd client/js
        node install .

 

# KARMA
* http://karma-runner.github.io/2.0/intro/installation.html
*  https://www.npmjs.com/package/karma-jasmine



# Must have doc links
* Debugging the grammar
https://ohmlang.github.io/editor/#30325d346a6e803cc35344ca218d8636


* The graphical elements used in the GUI:
* https://bootstrap-vue.js.org/
* https://gojs.net/latest/samples/sequenceDiagram.html



## TO BUILD A RELEASE:
In the project root:
 
    npm run build
 

Note that the produced file must be run in a web server in a structure like this:
 
        X-
        |- dist
            |- build.js
        |- index.html
 

index.html should contain the following:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>gaeditorweb2.1</title>
        </head>
        <body>
            <div id="app"></div>
            <script src="dist/build.js"></script>
        </body>
        </html v>
 



# License and other information

This project as a whole is licensed by Scania CV AB under the GNU General
Public License version 3.0 or any later version. For the avoidance of doubt,
Scania CV AB holds the patent
SE540377 *Methodology for testing using interactively changed traces* which
is related to this project. Should this patent be seen as covering whole or
parts of this project, this patent is explicitly considered part of the
*essential patent claims* as per the license.

