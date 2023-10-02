pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/robyrai/jenkins-pipeline-demo/'
        API_URL = 'http://localhost:8080'
    }

    stages {
        stage('Fetch Environment File') {
            steps {
                script {
                    
                    checkout([$class: 'GitSCM',
                                branches: [[name: '*/main']],
                                userRemoteConfigs: [[url: "${GITHUB_REPO}"]]
                    ])
                
                }
            }
        }

        stage('Call API') {
            steps {
                script {
                    def envFileContents = readFile('data.json') // Specify the path to your env file
                    echo envFileContents
                    //def apiUrl = "${API_URL}/your-api-endpoint"

                    // Use 'envFileContents' and 'apiUrl' in your HTTP request
                    // You may use the HTTP Request plugin or other methods to make the POST request
                }
            }
        }
    }
}
