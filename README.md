# linear-domino-game

This repository contains a generator and benchmark files for the Linear
Domino Placement game.  See the file doc/ldomino.pdf for more
information.

Subdirectories:

	doc:
		Benchmark documentation

	files:
		Benchmark files.  Total count=44.

	files-pgbddq:
		A version of the benchmark files generated
		for the PGBDDQ solver.  These include files
		specifying the BDD variable ordering.

	pgbddq:
		Code for the PGBDDQ QBF solver

	src:
		Code for the benchmark generator, and other utility programs

	results-depqbf:
		Results from running the DepQBF solver on the benchmark.
		Reproducing these results requires installing DepQBF

	results-ghostq:
		Results from running the GhostQ solver on the benchmark
		Reproducing these results requires installing GhostQ

	results-pgbddq:
		Results from running the PGBDDQ solver on the benchmark
		These results can be reproduced with the programs provided

