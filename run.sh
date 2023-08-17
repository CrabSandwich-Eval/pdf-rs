#!/bin/bash

for i in {0..7}
do
  docker run -t -d pdf_libafl_libfuzzer "/work/pdf/fuzz/fuzz.sh" "libafl_libfuzzer" $i
done
