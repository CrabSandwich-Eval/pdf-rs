#!/bin/bash

for i in {0..7}
do
  docker run -t -d pdf_libfuzzer "/work/pdf/fuzz/fuzz.sh" "libfuzzer" $i
done
