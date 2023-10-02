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
                    def apiUrl = "${API_URL}/echo"


                    def response = httpRequest(
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        requestBody: envFileContents,
                        url: apiUrl
                    )

                    def responseStatus = response.status
                    def responseBody = response.content

                    echo "API Response Status: ${responseStatus}"
                    echo "API Response Body: ${responseBody}"

                    // You can process the response as needed
                }
            }
        }
    }
}
