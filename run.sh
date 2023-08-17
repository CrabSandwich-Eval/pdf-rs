#!/bin/bash

docker build . -t pdf_cargo_libafl

for i in {0..7}
do
  docker run -t -d pdf_cargo_libafl "/work/pdf/fuzz/fuzz.sh" "cargo_libafl" $i
done
