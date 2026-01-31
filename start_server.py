#!/usr/bin/env python3
"""
Einfacher HTTP Server für Refresher 2026
Startet einen lokalen Webserver auf Port 8000
"""

import http.server
import socketserver
import os
from pathlib import Path

# Wechsle zum Verzeichnis dieser Datei
script_dir = Path(__file__).parent.absolute()
os.chdir(script_dir)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Füge CORS Headers hinzu
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()
    
    def log_message(self, format, *args):
        # Bessere Log-Ausgabe
        print(f"[{self.log_date_time_string()}] {format % args}")

try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✅ HTTP Server startet auf Port {PORT}")
        print(f"📂 Verzeichnis: {script_dir}")
        print(f"🌐 Öffne: http://localhost:{PORT}")
        print(f"📹 Video: http://localhost:{PORT}/video.html")
        print(f"\n💡 Drücke Ctrl+C um den Server zu beenden\n")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 48 or e.errno == 98:  # Port already in use
        print(f"❌ Port {PORT} ist bereits in Benutzung!")
        print(f"   Lösung: Schließe andere Prozesse oder nutze einen anderen Port")
    else:
        print(f"❌ Fehler: {e}")
except KeyboardInterrupt:
    print("\n\n👋 Server beendet")
