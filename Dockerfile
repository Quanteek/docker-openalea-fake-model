FROM quanteek/docker-openalea:latest
MAINTAINER quanteek

RUN mkdir -p .openalea/user_pkg
COPY ["__my package__/", "/home/user01/.openalea/user_pkg/"]

#workaround needed for having writing capabilities by openalea on its configuration directory
USER root
RUN chown -R user01:user01 .openalea
USER user01
