# Ubuntu with R. Other versions:
# https://rocker-project.org/images/versioned/r-ver.html
FROM rocker/r-ver:4.6.2

# curl: renv downloads packages with it
RUN apt-get update && apt-get install --yes \
    curl

# The project is mounted over /workspace, so the packages go in /opt
WORKDIR /workspace

# R packages in /opt/renv/library
RUN echo "RENV_PATHS_LIBRARY=/opt/renv/library" >> /usr/local/lib/R/etc/Renviron.site
COPY renv.lock .Rprofile ./
COPY renv/activate.R renv/
RUN Rscript -e "renv::restore()"
