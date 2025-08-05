#!/usr/bin/env python3
"""
PDF naar HTML conversie script voor executeurs_ontslaan_hoger_beroep directory
Converteert alle PDF bestanden naar HTML formaat voor Claude Code toegankelijkheid
"""

import os
import subprocess
import glob

def convert_pdf_to_html(pdf_path, html_path):
    """Converteer een PDF bestand naar HTML formaat"""
    try:
        # Probeer eerst pdftotext met HTML meta-informatie
        cmd = ['pdftotext', '-htmlmeta', pdf_path, html_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Succesvol geconverteerd: {os.path.basename(pdf_path)}")
            return True
        else:
            # Fallback: basis tekst extractie
            cmd = ['pdftotext', pdf_path, html_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Basis conversie: {os.path.basename(pdf_path)}")
                return True
            else:
                print(f"❌ Conversie gefaald: {os.path.basename(pdf_path)}")
                return False
                
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {e}")
        return False

def main():
    """Hoofdfunctie voor batch conversie"""
    base_dir = "/home/herbrand/rechtbank/executeurs_ontslaan_hoger_beroep"
    
    print("🔄 PDF naar HTML conversie voor executeurs_ontslaan_hoger_beroep directory")
    print("=" * 70)
    
    # Zoek alle PDF bestanden in directory
    pdf_pattern = os.path.join(base_dir, "*.pdf")
    all_pdfs = glob.glob(pdf_pattern)
    
    if not all_pdfs:
        print("❌ Geen PDF bestanden gevonden")
        return
    
    print(f"📄 Gevonden {len(all_pdfs)} PDF bestanden")
    print("-" * 40)
    
    successful = 0
    failed = 0
    
    for pdf_path in sorted(all_pdfs):
        # Maak HTML bestandsnaam
        html_path = pdf_path.replace('.pdf', '.html')
        
        # Skip als HTML al bestaat
        if os.path.exists(html_path):
            print(f"⏭️  Al geconverteerd: {os.path.basename(pdf_path)}")
            continue
        
        # Converteer PDF naar HTML
        if convert_pdf_to_html(pdf_path, html_path):
            successful += 1
        else:
            failed += 1
    
    print("-" * 40)
    print(f"📊 Conversie resultaten:")
    print(f"   ✅ Succesvol: {successful}")
    print(f"   ❌ Gefaald: {failed}")
    print(f"   📄 Totaal: {len(all_pdfs)}")
    
    if successful == len(all_pdfs):
        print("🎉 Alle conversies succesvol!")
    
    print("\n📋 Alle PDF bestanden zijn nu toegankelijk voor Claude Code analyse")

if __name__ == "__main__":
    main()