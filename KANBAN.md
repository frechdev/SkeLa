## Backlog
### Laufrichtungen von Treppen nur im svg
Die Laufrichtung von Treppen wird aktuell nur in der svg-Datei angezeigt, nicht jedoch im pdf. Vermutlich kann der aktuelle pdf-Interpreter nicht mit "Markern" umgehen.

### Fehlerhafte "TOP"- bzw "BOTTOM"-Anker-Abfrage an Shape-Objekten
Es ist vorgekommen, dass eine "TOP"- oder "BOTTOM"-Anker-Abfrage nicht den korrekten Anker-Punkt zurückgegeben hat. Stattdessen wurde der jeweils gegenteilige Anker-Punkt zurückgegeben.

### Dimensionierung in Furniture
Es soll konkret möglich sein, dass man auch den Einrichtungsplan bemaßen kann. Es ist zu Prüfen ob die Umsetzung so möglich ist, dass generell auch ein Element einem oder mehreren beliebigen Plantypen zugewiesen werden kann.

## Release: v00.001.04.00
### #0005: Dachschrägen
Es soll möglich sein, einen Dachschrägen (Slopes) im Plan einzeichnen zu können.

### #0004: TOP- und BOTTOM- Anker vertauscht
Wird als Position von auf einen "TOP"- oder "BOTTOM"-Anker einer Node referenziert, erscheint das Objekt entsprechend unten bei "TOP" oder oben bei "BOTTOM". Richtig wäre die Vertauschung

*Fehleranalyse:* Bei der Instanziierung des ```Anchor```-Enums wurde ```BOTTOM = (0.5, 1.0)``` und ```TOP = (0.5, 0.0)``` festgelegt (analog für ```TOP_LEFT``` usw.). Dies ist nicht korrekt, da die y-Achse der Zeichnung von "unten" nach "oben" in der Zeichnung geht.

*Fehlerbehandlung:* Die y-Koordinaten der Festlegungen für ```TOP```, ```BOTTOM```, ```TOP_LEFT```, ```TOP_RIGHT```, ```BOTTOM_LEFT```, ```BOTTOM_RIGHT``` wurden invertiert.

## Release: v00.001.03.00
### #0003: Dokument-Einheiten konsolidieren
Das Dokument soll im <svg>-Tag mit einer Breite und Höhe in cm sowie einer ViewBox, die alle im Dokument verwendeten Maße automatisch in cm umwandelt ausgestattet werden. Ggf. sind einige Maße im Dokument zu überarbeiten. Im idealfall wird dann auch der Maßstab über ein "scaling" möglich. Weitere daraus folgenden Vereinfachungen sind zu prüfung.

## Release: v00.001.02.00
### #0001: Seitenzähler bleibt bei "1" ohne "--svg"-Option
Wird die das Programm ausgeführt ohne "--svg"-Option, bleibt die Seitennummerierung bei "1".

*Fehleranalyse:* Das "page_counter"-Inkrement war fäschlicherweise innerhalb eines if-Blocks.

*Fehlerbehandlung:* Das "page_counter"-Inkrement wurde aus dem if-Block herausgenommen. Der Seitenzähler funktioniert nun unabhängig von der "--svg"-Option.

### #0002: Flächenberechnung der einzelnen Räume
Für jeden Raum soll automatisch die Fläche berechnet werden.

*Umsetzung:* Es wurde eine neue Klasse (AreaDimension) angelegt, die auf Basis eines Raums (Room) die Fläche berechnet. Der ConstructionPlanWriter instaziier zu jedem Room nun ein solches AreaDimension-Objekt.

## Release: v00.001.01.00

## Release: v00.001.00.00

