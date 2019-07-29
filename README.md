# ScansSeparate
---
Title: Navrh na zlepšení
...
#### popis problému 
Na AFE packu při skenování Spoo štítku, dochází k jeho naskenovaní oběma skenery, a to způsobí zachycení pozměněného kódů. 

Příklad:

| Skenováné | Zachicené 
| sp | sp

#### Řešení
Navrhuji použít program níže. 
Temto kód zabrání druhému skeneru k odeslání dat když už jeden odesílá.
