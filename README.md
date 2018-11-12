# sh1015-opendatalab
notebook (python+ROOT) based lab: measuring the Z boson mass with ATLAS open data.
Developed for third-year physics students to be used in Modern Physics course.
Use together with jupyter with python3+ROOT available, e.g. via Docker image pedwink/pyroot-notebook.

## Instructions
With Docker, start up the lab with 
`docker run -p 8080:8080 pedwink/opendatalab:sh1015-HT18`
This Docker image contains a snapshot of this repository, on top of pedwink/pyroot-notebook.
The jupyter server is launched and one can start working with the notebooks. 
If you don't have Docker, you can use it in 4-hour sessions via https://labs.play-with-docker.com/
