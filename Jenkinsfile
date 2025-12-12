pipeline {
    agent any

    stages {
        // Step 1: Just checking if we can build the container
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                // This is the command you ran manually earlier
                sh 'docker build -t my-python-app .'
            }
        }

        // Step 2: Now we run the tests inside the container
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // Here is a cool trick: We use the image we just built to run the tests!
                // We overwrite the default command to run the test file instead of app.py
                sh 'docker run --rm my-python-app python test_app.py' 
            }
        }
        
        // We aren't really "Deploying" to a server yet, 
        // but let's add the step so you see the structure.
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo 'Application deployed successfully!'
            }
        }
    }
}
