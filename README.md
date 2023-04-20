# Breast Cancer Example

**followed Machine Learning blog post from https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/**

This example notebook shows how to use Sagemaker's linear-learner to predict breast cancer. It demonstrates the following:
* Basic setup for using Sagemaker.
* converting datasets to the recordIO format used by the Amazon SageMaker algorithms and uploading to user provided S3 bucket.
* Training Sagemaker's linear learner on the data set.
* Hosting the trained model for scoring.
* Scoring using the trained model.

