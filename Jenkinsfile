pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
				// get some code from GIT 
               git "https://github.com/Satyajit0709/Satyajit_Python"
               echo 'Build phase'
            }
        }
		stage('Copy') {
            steps {
				echo 'Before we execute the batch file'
				bat "windows_copy.bat"
            }
        }
		stage('Test') {
            steps {
				echo 'Test Step'
            }
        }
    }
}