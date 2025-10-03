#!/bin/bash

# Bon Sojourn AI - GCP Deployment Script
# Make sure you have gcloud CLI installed and authenticated

set -e

# Configuration
PROJECT_ID=${PROJECT_ID:-"bon-sojourn"}
REGION=${REGION:-"us-central1"}
SERVICE_NAME="bon-sojourn-ai"

echo "🚀 Deploying Bon Sojourn AI to Google Cloud Platform..."

# Check if PROJECT_ID is set
if [ "$PROJECT_ID" = "your-project-id" ]; then
    echo "❌ Please set PROJECT_ID environment variable or update this script"
    echo "   export PROJECT_ID=your-actual-project-id"
    exit 1
fi

# Set the project
echo "📋 Setting project to: $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "🔧 Enabling required APIs..."
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

# Build and deploy using Cloud Build
echo "🏗️  Building and deploying with Cloud Build..."
gcloud builds submit --config cloudbuild.yaml .

echo "✅ Deployment complete!"
echo "🌐 Your service should be available at:"
gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)"

echo ""
echo "📝 To view logs:"
echo "   gcloud run services logs read $SERVICE_NAME --region=$REGION"

echo ""
echo "🔧 To update environment variables:"
echo "   gcloud run services update $SERVICE_NAME --region=$REGION --set-env-vars=KEY=VALUE"
