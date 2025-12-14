pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying Multi-Container Stack...'
		
		// Just stopping the old, running website to make sure the port is free to use.
		sh 'docker stop prod-website || true'
			
                // 1. Shut down any old version
                sh 'docker compose down || true'
                
                // 2. Start up new version in background
                // --build forces it to rebuild your Python image with the new code
                sh 'docker compose up -d --build'
            }
        }
        
        stage('Verify') {
             steps {
                 // Wait 5 seconds for DB to wake up
                 sleep 5
                 // Check if it's online
                 sh 'curl -f http://localhost:5000 || exit 1'
             }
        }
    }
}
