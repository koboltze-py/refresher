#!/usr/bin/env python3
"""
Video Generator für Refresher 2026 Schulung
Erstellt ein Video mit allen wichtigen Punkten
"""

import cv2
import numpy as np
import os
from pathlib import Path

# Konfiguration
OUTPUT_VIDEO = "refresher_2026_training.mp4"
FPS = 24
DURATION_PER_SLIDE = 6  # Sekunden pro Folie
TRANSITION_DURATION = 1  # Sekunden Übergangsdauer
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720

# Base Pfad zum Bildordner
BASE_PATH = r"C:\Users\DRKairport\OneDrive - Deutsches Rotes Kreuz - Kreisverband Köln e.V\Dateien von Erste-Hilfe-Station-Flughafen - DRK Köln e.V_ - !Gemeinsam.26\95_Ausbildung_Weiterbildung\Refresher Schulungen\Refresher 2026"

# Definieren Sie alle Folien mit Titeln und Beschreibungen
slides = [
    {
        "title": "Refresher 2026 - DRK Flughafen Köln",
        "subtitle": "Interaktive Schulung zur Handy-App",
        "image": None,
        "duration": 4
    },
    {
        "title": "1. Auftragsübersicht",
        "subtitle": "Überblick über alle Aufträge",
        "image": os.path.join(BASE_PATH, "Auftragsübersicht.jpg"),
        "duration": 6
    },
    {
        "title": "2. Tasks",
        "subtitle": "Aufgabenliste im System",
        "image": os.path.join(BASE_PATH, "Tasks.jpg"),
        "duration": 5
    },
    {
        "title": "3. Tasks auf dem Handy",
        "subtitle": "Mobile Ansicht der Aufgaben",
        "image": os.path.join(BASE_PATH, "Tasks Handy Korrektur.jpg"),
        "duration": 6
    },
    {
        "title": "4. Inbound Flüge",
        "subtitle": "Ankommende Flugzeuge verwalten",
        "image": os.path.join(BASE_PATH, "Inbound.jpg"),
        "duration": 5
    },
    {
        "title": "5. Outbound Flüge",
        "subtitle": "Abflügende Flugzeuge verwalten",
        "image": os.path.join(BASE_PATH, "Outbounds.jpg"),
        "duration": 5
    },
    {
        "title": "6. Mitarbeiter-Spalte",
        "subtitle": "Employees im Überblick",
        "image": os.path.join(BASE_PATH, "Spalte Emloyees.jpg"),
        "duration": 5
    },
    {
        "title": "7. Bordkarte scannen",
        "subtitle": "Wichtiger Schritt im Arbeitsablauf",
        "image": os.path.join(BASE_PATH, "Bordkarte Scannen.jpg"),
        "duration": 6
    },
    {
        "title": "8. Inbound richtig beenden",
        "subtitle": "Korrektes Abschließen von Inbound",
        "image": os.path.join(BASE_PATH, "Richtiges Beenden Inbound.jpg"),
        "duration": 6
    },
    {
        "title": "9. Outbound richtig beenden",
        "subtitle": "Korrektes Abschließen von Outbound",
        "image": os.path.join(BASE_PATH, "Richtiges Beenden Outbound.jpg"),
        "duration": 6
    },
    {
        "title": "10. Transferieren - Schritt 1",
        "subtitle": "Auftrag an Kollegen übertragen",
        "image": os.path.join(BASE_PATH, "Transferieren erster Schritt.jpg"),
        "duration": 5
    },
    {
        "title": "11. Transferieren - Schritt 2",
        "subtitle": "Kollegen auswählen",
        "image": os.path.join(BASE_PATH, "Transferieren zweiter Schritt.jpg"),
        "duration": 5
    },
    {
        "title": "12. Transferieren - Finaler Schritt",
        "subtitle": "Übertragung abschließen",
        "image": os.path.join(BASE_PATH, "Transferieren finaler Schritt.jpg"),
        "duration": 5
    },
    {
        "title": "13. Transfer-Übersicht",
        "subtitle": "An Kollegen übertragen",
        "image": os.path.join(BASE_PATH, "Transferieren an andere Kollegen.jpg"),
        "duration": 5
    },
    {
        "title": "14. Beispiel: Transit",
        "subtitle": "Umsteigende Passagiere verwalten",
        "image": os.path.join(BASE_PATH, "Beispiel Transit.jpg"),
        "duration": 6
    },
    {
        "title": "⚠️ WICHTIG: Fehler vermeiden",
        "subtitle": "Erzwungenes Drücken - NICHT machen!",
        "image": os.path.join(BASE_PATH, "Erzwungenes Drücken.jpg"),
        "duration": 6
    },
    {
        "title": "⚠️ Arbeitsverweigerung",
        "subtitle": "Wichtiger Hinweis zum Umgang",
        "image": os.path.join(BASE_PATH, "Arbeitsverweigerung ohne Namen.JPG"),
        "duration": 6
    },
    {
        "title": "⚠️ No Flight - Inbound",
        "subtitle": "Flug wurde gestrichen",
        "image": os.path.join(BASE_PATH, "No Flight Inbound.jpg"),
        "duration": 5
    },
    {
        "title": "⚠️ No Flight - Outbound",
        "subtitle": "Flug wurde gestrichen",
        "image": os.path.join(BASE_PATH, "No Flight Outbound.jpg"),
        "duration": 5
    },
    {
        "title": "17. Chatprogramm",
        "subtitle": "Kommunikation mit Kollegen",
        "image": os.path.join(BASE_PATH, "Chatprogramm.jpg"),
        "duration": 5
    },
    {
        "title": "18. Notes - Notizen",
        "subtitle": "Notizen erfassen",
        "image": os.path.join(BASE_PATH, "Notes.jpg"),
        "duration": 5
    },
    {
        "title": "19. Notes-Übersicht",
        "subtitle": "Alle Notizen im Überblick",
        "image": os.path.join(BASE_PATH, "Notesübersichtjpg.jpg"),
        "duration": 5
    },
    {
        "title": "✓ Aussehen am Abholort",
        "subtitle": "So sollte es aussehen",
        "image": os.path.join(BASE_PATH, "Aussehen am Abholort.jpg"),
        "duration": 5
    },
    {
        "title": "✗ Aussehen NICHT am Abholort",
        "subtitle": "Vermeiden!",
        "image": os.path.join(BASE_PATH, "Aussehen NICHT am Abholort.jpg"),
        "duration": 5
    },
    {
        "title": "20. Disregarden",
        "subtitle": "Auftrag verwerfen",
        "image": os.path.join(BASE_PATH, "Disregarden.jpg"),
        "duration": 5
    },
    {
        "title": "Schulung abgeschlossen!",
        "subtitle": "Vielen Dank für die Aufmerksamkeit",
        "image": None,
        "duration": 4
    }
]

def create_blank_frame(text1="", text2="", color=(30, 60, 140)):
    """Erstelle einen leeren Frame mit Text"""
    frame = np.ones((VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
    frame[:] = color
    
    if text1:
        cv2.putText(frame, text1, (60, 200), cv2.FONT_HERSHEY_DUPLEX, 2.5, (255, 255, 255), 3)
    if text2:
        cv2.putText(frame, text2, (60, 280), cv2.FONT_HERSHEY_DUPLEX, 1.5, (200, 220, 255), 2)
    
    return frame

def resize_image_to_frame(image, target_width=1000, target_height=550, bg_color=(50, 50, 50)):
    """Resize Bild proportional und zentriere es"""
    h, w = image.shape[:2]
    scale = min(target_width / w, target_height / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    # Erstelle Background
    frame = np.ones((VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
    frame[:] = bg_color
    
    # Zentriere das Bild
    x_offset = (VIDEO_WIDTH - new_w) // 2
    y_offset = ((VIDEO_HEIGHT - 100) - new_h) // 2
    
    frame[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
    
    return frame

def add_text_overlay(frame, title="", subtitle=""):
    """Füge Text-Overlay hinzu"""
    frame_copy = frame.copy()
    
    # Dunkler Hintergrund für Text
    cv2.rectangle(frame_copy, (0, VIDEO_HEIGHT - 100), (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0), -1)
    cv2.rectangle(frame_copy, (0, VIDEO_HEIGHT - 100), (VIDEO_WIDTH, VIDEO_HEIGHT), (255, 255, 255), 2)
    
    if title:
        cv2.putText(frame_copy, title, (20, VIDEO_HEIGHT - 55), cv2.FONT_HERSHEY_DUPLEX, 1.3, (255, 255, 255), 2)
    if subtitle:
        cv2.putText(frame_copy, subtitle, (20, VIDEO_HEIGHT - 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (150, 200, 255), 1)
    
    return frame_copy

def generate_video():
    """Generiere das Video"""
    print("Starte Video-Generierung...")
    print(f"Output: {OUTPUT_VIDEO}")
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))
    
    frame_count = 0
    total_frames_estimated = sum(s.get("duration", DURATION_PER_SLIDE) * FPS for s in slides)
    
    for slide_idx, slide in enumerate(slides):
        print(f"\nProcessing slide {slide_idx + 1}/{len(slides)}: {slide['title']}")
        
        duration = slide.get("duration", DURATION_PER_SLIDE)
        num_frames = int(duration * FPS)
        
        if slide["image"] and os.path.exists(slide["image"]):
            # Lade Bild
            try:
                image = cv2.imread(slide["image"])
                if image is None:
                    raise ValueError("Bild konnte nicht geladen werden")
                
                frame = resize_image_to_frame(image)
            except Exception as e:
                print(f"  ⚠️ Fehler beim Laden: {e}")
                frame = create_blank_frame(slide['title'], slide['subtitle'])
        else:
            # Erstelle Blank Frame
            frame = create_blank_frame(slide['title'], slide['subtitle'])
        
        # Füge Text-Overlay hinzu
        frame = add_text_overlay(frame, slide['title'], slide['subtitle'])
        
        # Schreibe Frames
        for i in range(num_frames):
            out.write(frame)
            frame_count += 1
            if frame_count % (FPS * 5) == 0:
                print(f"  ✓ {frame_count} frames geschrieben...")
    
    out.release()
    print(f"\n✅ Video erfolgreich erstellt: {OUTPUT_VIDEO}")
    print(f"Total frames: {frame_count}")
    print(f"Duration: {frame_count / FPS:.1f} Sekunden")

if __name__ == "__main__":
    generate_video()
