package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"
)

func main() {
	// Set up the static file server
	staticDir := "./content"

	// Create a simple file server handler
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		filePath := filepath.Join(staticDir, r.URL.Path)

		// Check if the path is a directory
		if stat, err := os.Stat(filePath); err == nil && stat.IsDir() {
			// Try to serve index.html from the directory
			indexPath := filepath.Join(filePath, "index.html")
			if _, err := os.Stat(indexPath); err == nil {
				http.ServeFile(w, r, indexPath)
				return
			}
		}

		// Check if file exists at the constructed path
		if _, err := os.Stat(filePath); err == nil {
			http.ServeFile(w, r, filePath)
			return
		}

		// Use the file server for all other requests
		fileServer := http.FileServer(http.Dir(staticDir))
		fileServer.ServeHTTP(w, r)
	})

	// Add simple API endpoints
	http.HandleFunc("/api/status", statusHandler)
	http.HandleFunc("/api/info", infoHandler)

	// Get port from environment or use default
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Println("Bewindvoerder Controle Website - Listening on :" + port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"status": "ok", "message": "Bewindvoerder Controle Website is running"}`)
}

func infoHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// Get some basic info about the content directory
	staticDir := "./content"
	files := []string{}

	// Check if static directory exists
	if _, err := os.Stat(staticDir); os.IsNotExist(err) {
		fmt.Fprintf(w, `{
			"static_dir": "%s",
			"status": "directory not found",
			"total_files": 0,
			"sample_files": []
		}`, staticDir)
		return
	}

	err := filepath.Walk(staticDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			relPath, _ := filepath.Rel(staticDir, path)
			files = append(files, relPath)
		}
		return nil
	})

	if err != nil {
		fmt.Fprintf(w, `{
			"static_dir": "%s",
			"status": "error reading directory",
			"error": "%s",
			"total_files": 0,
			"sample_files": []
		}`, staticDir, err.Error())
		return
	}

	fmt.Fprintf(w, `{
		"static_dir": "%s",
		"status": "ok",
		"total_files": %d,
		"sample_files": %v
	}`, staticDir, len(files), files[:min(5, len(files))])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
