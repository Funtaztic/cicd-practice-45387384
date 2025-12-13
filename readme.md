CI/CD Practice with Flask, Docker, and Jenkins
A simple Python Flask application demonstrating a complete CI/CD pipeline. The project uses Docker for containerization and Jenkins to automate the build, test, and deployment processes.

Project Structure
app.py: The main Flask application that serves a web page and performs simple calculations.

test_app.py: Unit tests using Python's built-in unittest framework to verify application logic.

Dockerfile: Instructions to package the application and dependencies into a lightweight Docker container.

Jenkinsfile: The pipeline script defining the Build, Test, and Deploy stages.

requirements.txt: List of Python dependencies (Flask).

Prerequisites
Docker installed on the host machine.

Jenkins installed (running in a Docker container with access to the host Docker socket).

Git for version control.

Manual Usage
To build and run the application locally without Jenkins:

Build the Docker image: docker build -t my-flask-app .

Run the container: docker run -p 5000:5000 my-flask-app

Access the application: Open a browser and go to http://localhost:5000

CI/CD Pipeline (Jenkins)
The included Jenkinsfile defines the following automated stages:

Build: Creates the Docker image from the source code.

Test: Runs the unit tests inside the container. If tests fail, the pipeline stops.

Deploy: Stops any existing instance of the application and starts a new container on port 5000 in detached mode.

Setting up in Jenkins
Create a new "Pipeline" item in Jenkins.

Under "Pipeline Definition", select "Pipeline script from SCM".

Select "Git" and enter the repository URL.

Set the branch to */main.

Save and click "Build Now".

Comparison
Manual Run: Requires typing commands; runs in the foreground.

Pipeline Run: Automated; runs tests before deploying; deploys in the background (detached mode) automatically.
