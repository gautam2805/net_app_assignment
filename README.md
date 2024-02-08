# Jenkins Pipeline for Python App Deployment

   This Jenkins pipeline automates the build, testing, and deployment workflow for a simple Python application. The primary functionality includes building a Docker image, pushing it to the Docker registry, and updating the deployment configuration for subsequent deployment through ArgoCD. The deployment process is orchestrated using Jenkins, Minikube, and ArgoCD on a specified VM (64.227.169.89).

## Workflow Overview
- Checkout Source Code:

The pipeline starts by checking out the source code from the specified repository. (optional for scm polling)

- Build and Push Docker Image:

The Python application is packaged into a Docker image.
The image is tagged with the build number and pushed to the Docker registry at gautam2805/netappassignment:${BUILD_NUMBER}.

- Update APP Deployment File:

The Jenkins pipeline updates the deployment configuration file (deployment.yml) located in the assignment_app_manifest directory.
The replaceImageTag placeholder in the deployment file is substituted with the current build number.
- Commit and Push to GitHub:

The updated deployment file is committed to the GitHub repository (net_app_assignment).
The commit includes a message indicating the updated deployment image version.

## Usage Instructions
### Prerequisites
Jenkins, Minikube, and ArgoCD are deployed on the VM (64.227.169.89).

- Jenkins Pipeline Configuration
  Configure Jenkins credentials:

- Ensure Docker registry credentials are added to Jenkins as "docker-cred".
  Add GitHub credentials with the ID "github" for repository access.
  Create a Jenkins pipeline job with the provided Jenkinsfile:

- Configure the job to use the appropriate Jenkins agent.
  Ensure the pipeline script references the correct paths and repository details.
  Run the Jenkins pipeline:

- Trigger the pipeline manually or configure a webhook for automatic execution on code changes.
  Monitor the Pipeline Execution:

- Observe the Jenkins console output for each stage, including Docker image build, push, and GitHub commit.
- Integration with ArgoCD
- Ensure that ArgoCD is set up and configured to monitor the GitHub repository.
- ArgoCD will automatically detect changes in the deployment.yml file and trigger the deployment of the updated Docker image.

### Note: Uncomment and configure the Python testing stage (Build and Test (Pytest)) in the Jenkinsfile if additional testing is required for the Python application.