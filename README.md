# aws-secrets-lambda
Lambda to retrieve secrets (SecureString type parameters from System Manager) from AWS.

## Install
Run `pip install`. All dependencies are listed in the `lambda/requirements.txt`.

## Build & Deploy
The build and deploy process relies on (AWS SAM CLI)[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html]. At the root level, run `sam build` and `sam deploy -g`.

Note: The `-g` option is for first time template deploys. The `samconfig.toml` file it generates will designate an S3 bucket for storage. If you wish to specify a different S3, you can simply change this option and use `sam deploy` for all future deploys
