# Use the official Alpine Linux image as a base
FROM alpine:latest

# Set a label for the image
LABEL maintainer="student@example.com"
	
# Set an environment variable
# ENV MESSAGE="Hello, Dockerfile!"

COPY welcome.txt /welcome.txt
CMD cat /welcome.txt
	
# Define the command to run when the container starts
# CMD echo $MESSAGE
CMD ["/bin/sh"]
