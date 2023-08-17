#!/bin/bash

docker build . -t pdf_libafl_libfuzzer

for i in {0..7}
do
  docker run -t --name pdf_libafl_libfuzzer-"$i" -d pdf_libafl_libfuzzer "/work/pdf/fuzz/fuzz.sh" "libafl_libfuzzer" $i
done

for i in {0..7}
do
  docker wait pdf_libafl_libfuzzer-"$i"
done
