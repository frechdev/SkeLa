## Backlog
### Dachschrägen
Es soll möglich sein, einen Dachschrägen im Plan einzeichnen zu können.

### Laufrichtungen von Treppen nur im svg
Die Laufrichtung von Treppen wird aktuell nur in der svg-Datei angezeigt, nicht jedoch im pdf. Vermutlich kann der aktuelle pdf-Interpreter nicht mit "Markern" umgehen.

### Fehlerhafte "TOP"- bzw "BOTTOM"-Anker-Abfrage an Shape-Objekten
Es ist vorgekommen, dass eine "TOP"- oder "BOTTOM"-Anker-Abfrage nicht den korrekten Anker-Punkt zurückgegeben hat. Stattdessen wurde der jeweils gegenteilige Anker-Punkt zurückgegeben.

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

