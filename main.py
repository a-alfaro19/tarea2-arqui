import random
from datetime import datetime
from pathlib import Path

from CISC import CISC
from Memory import Memory
from RISC import RISC


def save_results_files(A, B,
    cisc_result_base, risc_result_base, n,
    mem, cisc, risc,
    prefix="results_cisc_risc"
):
    """ Creates a txt file with the program results.

    :param A: Vector A
    :param B: Vector B
    :param cisc_result_base: CISC result base
    :param risc_result_base: RISC result base
    :param n: Vector size
    :param mem: Processor memory
    :param cisc: CISC architecture
    :param risc: RISC architecture
    :param prefix: Text file prefix
    :return: None
    """
    # Prepare Data
    cisc_dump = mem.dump_range(cisc_result_base, n)
    risc_dump = mem.dump_range(risc_result_base, n)
    cisc_vec = [val for _, val in cisc_dump]
    risc_vec = [val for _, val in risc_dump]
    expected = [A[i] + B[i] for i in range(n)]
    ok = (cisc_vec == risc_vec == expected)

    # Folder to store results
    base_dir = Path(__file__).resolve().parent
    results_dir = base_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Set date and path
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    txt_path = results_dir / f"{prefix}_{ts}.txt"

    # ---- TXT ----
    with txt_path.open("w", encoding="utf-8") as f:
        f.write("=== CISC RESULTS ===\n")
        f.write(f"Result vector (mem[{cisc_result_base}..{cisc_result_base + n - 1}]): {cisc_dump}\n")
        f.write(f"Executed instructions: {cisc.stats.instructions}\n")
        f.write(f"Total cycles: {cisc.stats.cycles}\n\n")

        f.write("=== RISC RESULTS ===\n")
        f.write(f"Result vector (mem[{risc_result_base}..{risc_result_base + n - 1}]): {risc_dump}\n")
        f.write(f"Executed instructions: {risc.stats.instructions}\n")
        f.write(f"Total cycles: {risc.stats.cycles}\n\n")

        f.write("Verification: CISC and RISC results match!\n" if ok else "Verification FAILED\n")

    print(f"[OK] TXT saved on: {txt_path.resolve()}")


if __name__ == "__main__":
    mem = Memory()

    # Vectors
    A = [random.randint(1,100) for i in range(100)]
    B = [random.randint(1,100) for i in range(100)]
    n = 10

    # - CISC
    cisc_pair_base = 0
    cisc_result_base = 50
    for i in range(n):
        mem.write(cisc_pair_base + 2*i, A[i])
        mem.write(cisc_pair_base + 2*i + 1, B[i])

    # - RISC
    risc_a_base = 100
    risc_b_base = 110
    risc_result_base = 120
    for i in range(n):
        mem.write(risc_a_base + i, A[i])
        mem.write(risc_b_base + i, B[i])

    # Execute CISC program
    cisc = CISC(mem)
    cisc.run_program(interleaved_base=cisc_pair_base, result_base=cisc_result_base, n=n)

    # Execute RISC program
    risc = RISC(mem)
    risc.run_program(a_base=risc_a_base, b_base=risc_b_base, result_base=risc_result_base, n=n)

    # Show results
    print("=== CISC RESULTS ===")
    print(f"Result vector (mem[{cisc_result_base}...{cisc_result_base + n-1}]): {mem.dump_range(cisc_result_base, n)}")
    print(f"Executed instructions: {cisc.stats.instructions}")
    print(f"Totals cycles: {cisc.stats.cycles}")

    print("=== RISC RESULTS ===")
    print(f"Result vector (mem[{risc_result_base}...{risc_result_base + n-1}]): {mem.dump_range(risc_result_base, n)}")
    print(f"Executed instructions: {risc.stats.instructions}")
    print(f"Totals cycles: {risc.stats.cycles}")

    # Check both results
    cisc_result = [val for _, val in mem.dump_range(cisc_result_base, n)]
    risc_result = [val for _, val in mem.dump_range(risc_result_base, n)]
    assert cisc_result == risc_result == [A[i] + B[i] for i in range(n)], "Vectors dose not match!"
    print("\nVerification: CISC and RISC results match!")

    # Save Results
    save_results_files(A, B, cisc_result_base, risc_result_base, n, mem, cisc, risc, prefix="results_cisc_risc")
