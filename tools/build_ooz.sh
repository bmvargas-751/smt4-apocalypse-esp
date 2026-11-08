#!/usr/bin/env bash
# Descarga y compila ooz (descompresor de Oodle de código abierto, GPL-3.0) para
# leer los paquetes de SMT V con tools/smt5v.py. Queda fuera del repo:
# ../smt4a-local/ooz/ (código en src/, biblioteca en libooz.so). Necesita git y g++.
set -euo pipefail
DEST="$(cd "$(dirname "$0")/../.." && pwd)/smt4a-local/ooz"
COMMIT=360fc8a                       # rarten/ooz, la versión revisada
mkdir -p "$DEST"
if [ ! -d "$DEST/src" ]; then
  git clone -q https://github.com/rarten/ooz.git "$DEST/src"
fi
git -C "$DEST/src" checkout -q "$COMMIT"
SRC="$DEST/src"
g++ -O2 -fPIC -shared -mssse3 -msse4.1 -w -I"$SRC" -o "$DEST/libooz.so" \
  "$SRC"/kraken.cpp "$SRC"/bitknit.cpp "$SRC"/lzna.cpp "$SRC"/compress.cpp \
  "$SRC"/compr_entropy.cpp "$SRC"/compr_kraken.cpp "$SRC"/compr_leviathan.cpp \
  "$SRC"/compr_match_finder.cpp "$SRC"/compr_mermaid.cpp "$SRC"/compr_multiarray.cpp \
  "$SRC"/compr_tans.cpp
echo "Listo: $DEST/libooz.so"
