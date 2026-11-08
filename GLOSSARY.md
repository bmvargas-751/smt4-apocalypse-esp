# Glosario

Términos fijos de la traducción. La guía de estilo está en [STYLE.md](STYLE.md).

## Reglas

- **G-1** Los términos que IVA comparte con *SMT V: Vengeance* (demonios, habilidades, razas, estados, objetos) llevan el de la traducción oficial de SMT V al español. Se toma el término, no el registro, porque esa traducción es casi seguro de España. [PLAN]
- **G-2** Lo propio de IV e IVA se decide aquí. Hasta que esté decidido, el término va a [PENDING.md](PENDING.md) con una propuesta. [PLAN]
- **G-3** Un término de esta tabla se usa igual en todo el juego. `tools/check.py` avisa cuando el inglés lo tiene y el español no (`glosario`). [Encargo §6]

## Cómo se arma

1. `tools/smt5v.py candidates` empareja los nombres de SMT V en inglés y en español y busca cada uno en IVA. El resultado queda fuera del repo (`../smt4a-local/glossary-candidates.tsv`), porque es texto de otro juego.
2. El terminólogo revisa los candidatos y propone las filas: *oficial* si es el mismo término en los dos juegos, o *por decidir* si el término inglés significa otra cosa en IVA.
3. Las filas *oficial* entran a la tabla. Las *por decidir* van a [PENDING.md](PENDING.md) para que las decida el usuario.

## Términos

| Inglés | Español | Fuente | Nota |
|---|---|---|---|
