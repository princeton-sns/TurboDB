# TurboDB

The repository is organized as follows:

```
deps/           # scripts for installing dependencies.
```

Current codebase is spread over a few repositories:

- CockroochDB (modified for TurboDB):
	- TurboDB: https://github.com/jl3953/cockroach3.0/tree/insertWritesTpccTemp
	- Baseline: https://github.com/jl3953/cockroach3.0/tree/new-cloudlab

- Cicada (modified for TurboDB): https://github.com/jl3953/cicada-engine/tree/insertWritesTpcc

- Test scripts: https://github.com/jl3953/thermopylae_tests_scripts/tree/insertWritesTpcc

- Graph generation scripts: https://github.com/jl3953/thermopylae_graphs

## Getting Started

Please build and install all dependencies following instructions [here](https://github.com/princeton-sns/TurboDB/deps).


## BibTex
```
@inproceedings{lam2024accelerating,
  title={Accelerating Skewed Workloads With Performance Multipliers in the $\{$TurboDB$\}$ Distributed Database},
  author={Lam, Jennifer and Helt, Jeffrey and Lloyd, Wyatt and Lu, Haonan},
  booktitle={21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)},
  year={2024}
}
```

## Acknowledgements

This work was supported by the National Science Foundation under
Grant No. CNS 2241719, CNS 1824130, CNS 2327609, and CNS 2321724.
All opinions, findings, conclusions, or recommendations expressed
are those of the authors and do no necessarily reflect the views
of the National Science Foundation.
