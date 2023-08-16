#!/usr/bin/python3
import sys
import subprocess
import os
benchmark = os.environ["BENCHMARK"]

def run():
    assert len(sys.argv) == 3
    fuzzer = sys.argv[1]
    core = sys.argv[2]

    time = "8h" if "FUZZER_DEBUG" not in os.environ else "5s" 

    if fuzzer == "libfuzzer":
        command = ["timeout", "-s", "SIGKILL", time, "taskset", "-c", core, "./{}".format(benchmark), "-fork=1", "-ignore_ooms=1", "-ignore_timeouts=1", "-ignore_crashes=1", "-detect_leaks=0", "-artifact_prefix=./output", "./output", "./seeds"]
        subprocess.run(command)
    elif fuzzer == "cargo_libafl":
        command = ["timeout", "-s", "SIGKILL", time, "./{}".format(benchmark), "--cores", core, "--input", "./seeds", "--output", "./output"]
        subprocess.run(command)
    elif fuzzer == "libafl_libfuzzer":
        command = ["timeout", "-s", "SIGKILL", time, "taskset", "-c", core, "./{}".format(benchmark), "-fork=1", "-ignore_ooms=1", "-ignore_timeouts=1", "-ignore_crashes=1", "-detect_leaks=0", "-artifact_prefix=./output", "./output", "./seeds"]
        subprocess.run(command)

    print("DONE")

def coverage():
    cov = ["cargo", "fuzz", "coverage", benchmark, "./output"]
    if sys.argv[1] == "libfuzzer" or "libafl_libfuzzer":
        llvm_cov = "/root/.rustup/toolchains/nightly-2023-08-14-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-cov"
    else:
        llvm_cov = "/root/.rustup/toolchains/nightly-2022-07-20-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-cov"


    generate = [llvm_cov, "show", "./target/x86_64-unknown-linux-gnu/coverage/x86_64-unknown-linux-gnu/release/{}".format(benchmark), "--format=html", "--instr-profile=./coverage/{}/coverage.profdata".format(benchmark), "-o", "result/"]

    subprocess.run(cov)
    subprocess.run(generate)

    # 
if __name__ == '__main__':
    run()
    coverage()