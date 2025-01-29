### Backlog
#### Dachschrägen
Es soll möglich sein, einen Dachschrägen im Plan einzeichnen zu können.


### Release: v00.001.01.01
#### #0001: Seitenzähler bleibt bei "1" ohne "--svg"-Option
Wird die das Programm ausgeführt ohne "--svg"-Option, bleibt die Seitennummerierung bei "1".

*Fehleranalyse:* Das "page_counter"-Inkrement war fäschlicherweise innerhalb eines if-Blocks.

*Fehlerbehandlung:* Das "page_counter"-Inkrement wurde aus dem if-Block herausgenommen. Der Seitenzähler funktioniert nun unabhängig von der "--svg"-Option.

### Release: v00.001.01.00

### Release: v00.001.00.00

