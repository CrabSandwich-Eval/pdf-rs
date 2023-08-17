#!/bin/bash

docker build . -t pdf_libfuzzer

for i in {0..7}
do
  docker run -t --name pdf_libfuzzer-"$i" -d pdf_libfuzzer "/work/pdf/fuzz/fuzz.sh" "libfuzzer" $i
done

for i in {0..7}
do
  docker wait pdf_libfuzzer-"$i"
done

