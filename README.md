# OpenDataZmassLab
This repository contains a notebook setup (python+ROOT) that allows measuring the Z boson mass with ATLAS open data.
The lab was originally developed by Edvin Sidebo in 2018 for third-year physics students taking a Modern Physics course at KTH Royal Institute of Technology in Stockholm, Sweden. Use together with jupyter with python3+ROOT available, e.g. via Docker image cohm/pyroot-notebook.

## Instructions
With Docker, start up the lab with 
`docker run -p 3000:8080 kthatlas/opendatalab:SH1015`
This Docker image contains a snapshot of this repository, on top of cohm/pyroot-notebook.
The jupyter server is launched and one can start working with the notebooks. 
If you don't have Docker, you can use it in free four-hour sessions via https://labs.play-with-docker.com/
