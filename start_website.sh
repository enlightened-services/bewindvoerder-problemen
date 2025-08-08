#!/bin/bash

echo "🚀 Starting Bewindvoerder Controle Website..."
echo "📍 Project: A.P. Hofker-Spaan - Thorin Eijkelenboom"
echo "📊 Status: Bewijsmateriaal georganiseerd - Klaar voor juridische procedures"
echo ""

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "❌ Error: Go is not installed"
    echo "Please install Go from https://golang.org/"
    exit 1
fi

# Build and run the website
echo "🔨 Building website..."
go build -o bewindvoerder-website main.go

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "🌐 Starting server on http://localhost:8080"
    echo "📁 Content directory: ./content"
    echo "📄 Main page: http://localhost:8080"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""
    
    # Run the website
    ./bewindvoerder-website
else
    echo "❌ Build failed!"
    exit 1
fi
