# 🌐 Bewindvoerder Controle Website

## 📋 Project Overzicht
Moderne webapplicatie voor de controle van de eindafrekening van A.P. Hofker-Spaan door Thorin Eijkelenboom.

## 🚀 Quick Start

### Vereisten
- Go 1.21 of hoger
- Bash shell

### Start de Website
```bash
./start_website.sh
```

Of handmatig:
```bash
go build -o bewindvoerder-website main.go
./bewindvoerder-website
```

### Website URL
**http://localhost:8080**

## 📁 Project Structuur

```
eijkelenboom/
├── main.go                    # Go webserver
├── start_website.sh          # Start script
├── go.mod                    # Go module
├── content/                  # Website content
│   ├── index.html           # Hoofdpagina
│   ├── controle/            # Controle rapportage
│   ├── bewijsmateriaal/     # Bewijsmateriaal
│   ├── juridisch/           # Juridische procedures
│   └── documenten/          # PDF downloads
└── README-website.md        # Deze file
```

## 🎯 Website Features

### 📊 Project Overzicht
- **Controle Score:** 0/10 (Catastrofaal)
- **Financiële Impact:** €45.803,48
- **Bewijsmateriaal:** 881 bestanden
- **Juridische Procedures:** 3 templates

### 📋 Secties
1. **Controle Rapportage** - Uitgebreide analyse
2. **Bewijsmateriaal** - 881 georganiseerde bestanden
3. **Juridische Procedures** - Templates voor indiening
4. **Documenten** - PDF downloads

### 🚨 Kritieke Bevindingen
- Catastrofale beoordeling eindafrekening
- €45.803,48 directe financiële schade
- 881 bewijsstukken van frauduleuze praktijken
- 3 juridische procedures in voorbereiding

## 📞 Contactgegevens

### Aangeklaagde
**Thorin Eijkelenboom**  
E&M financieel beheer  
thorin@em-financieelbeheer.nl  
Postbus 1105, 1400 BC BUSSUM  
KVK: 88775089

### Nalatenschap
**A.P. Hofker-Spaan**  
Overleden: 27 november 2024  
Plaats: Laren  
Status: Juridische procedures in voorbereiding

## 🔧 Technische Details

### Go Webserver
- **Port:** 8080 (configureerbaar via PORT environment)
- **Static Files:** ./content directory
- **API Endpoints:** /api/status, /api/info

### Frontend
- **Framework:** Tailwind CSS
- **Design:** Modern, responsive
- **Colors:** Primary (#2c3e50), Secondary (#e74c3c)

### Content
- **HTML:** Moderne, toegankelijke markup
- **PDFs:** Direct download links
- **Navigation:** Intuïtieve sectie navigatie

## 📈 Status
**Bewijsmateriaal georganiseerd - Klaar voor juridische procedures**

---

**Datum:** 5 augustus 2024  
**Project:** Bewindvoerder Controle - A.P. Hofker-Spaan
