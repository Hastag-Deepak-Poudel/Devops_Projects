@Library('myLibrary') _
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                hello("samwise")
            }
        }
    }
}

