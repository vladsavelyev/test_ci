#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
OUT_BUCKET="${DIR}/test_run"
test_ci "${DIR}/toy.g.vcf.bgz" "$OUT_BUCKET/toy.mt"
ls $OUT_BUCKET
test -e $OUT_BUCKET/toy.mt/_SUCCESS
