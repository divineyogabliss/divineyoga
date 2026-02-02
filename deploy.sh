#!/bin/bash
set -e

APP_DIR="/home/ec2-user/apps/divineyoga"
REPO_URL="https://github.com/divineyogabliss/divineyoga.git"

echo "🚀 Starting deployment..."

# Ensure base directory exists
mkdir -p /home/ec2-user/apps

# First-time clone
if [ ! -d "$APP_DIR/.git" ]; then
  echo "📦 Cloning repository for the first time..."
  git clone "$REPO_URL" "$APP_DIR"
fi

cd "$APP_DIR"

echo "🔄 Pulling latest changes..."
git pull origin main

echo "🐳 Building Docker image..."
docker build -t divineyoga .

echo "🛑 Stopping old container (if exists)..."
docker stop divineyoga || true
docker rm divineyoga || true

echo "▶️ Starting new container..."
docker run -d \
  --name divineyoga \
  --env-file .env \
  -p 8000:8000 \
  --restart unless-stopped \
  divineyoga

echo "✅ Deployment completed successfully!"
