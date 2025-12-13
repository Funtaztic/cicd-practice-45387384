pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                // I renamed the image to 'my-flask-app' to match your manual test
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // We test the image we just built
                sh 'docker run --rm my-flask-app python test_app.py' 
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                
                // 1. CLEANUP: Stop and remove any old container named 'prod-website'
                // The '|| true' part means "If you don't find one, don't crash, just keep going"
                sh 'docker stop prod-website || true'
                sh 'docker rm prod-website || true'
                
                // 2. LAUNCH: Run the new container
                // -d : Detached mode (run in background, don't block Jenkins)
                // -p : Map port 5000 so you can see it
                // --name : We name it 'prod-website' so we can easily find/kill it next time
                sh 'docker run -d -p 5000:5000 --name prod-website my-flask-app'
            }
        }
    }
}
