# RehKiz
Save the Bambi!

## Ausgangslage
- Team mit vier Personen
  - Pilot
  - Pilotassistenz (Kamera überwachung)
  - Retter (2x Rehkitz einsammeln)
- Drohne mit Wärmebild und Kamera an Gimbal
- Controller mit Bildschirm für Wärmebild und Kamerabild
- Funkkommunikation zwischen Pilotassistenz und Retter
- Suchzeitraum zwischen 04:00 - 08:00 Uhr (vor Sonnenaufgang)
  - Saison: Ab mitte April bis Juni

### Ablauf
- Std. Flughöhe 60m
  - Resultierender Suchkreis ~30 m Durchmesser
  - Fluggeschwindigkeit ca. 3-4 m/s
- Vorgefertigte Flugbahnen
  - Pilot betrachtet interessante Punkte aus der Nähne

### Hardware
- DJI Mavic 2ae
  - [Link DJI]([https://enterprise.dji.com/mavic-3-enterprise](https://www.dji.com/ch/support/product/mavic-2-enterprise-advanced))
  - Visuelle Kamera: 1/2” CMOS, Effective Pixels: 48 M, 1920×1080@30fps, 35 mm format equivalent: 24 mm
  - Thermal Kamera: Uncooled VOx Microbolometer, 640×512 @30Hz, 35 mm format equivalent: Approx. 38mm
  - Flugzeit ca. 15 min pro Akku
- Bildübertragung auf externes Device via Dongle oder HDMI in 1080p@30fps
- Controller: RC Pro
 
### Datengrundlage
- Thermale und Visuelle Videos
- MP4
- 30fps
- Thermales Format: 640x512
  - Die Graustufen des Bildes werden Dynamisch angepasst (Histogrammausgleich o.ä.)
- Visuelles Format: 1920x1080
- ~51 GB Videomaterial

### Offene Fragen
- Können Metainformationen zu Flughöhe, Koordinaten, Zoomfaktor etc. ebenfalls auf dem externen Device verfügbar gemacht werden?
- Reicht er die GPS Position auf der Karte zu markieren um die Retter zum Kitz zu führen? (Genauigkeit?)
