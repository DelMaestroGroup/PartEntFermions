# tV_diagonalize

A Julia exact diagonalization code for the [tV model](https://en.wikipedia.org/wiki/Bose%E2%80%93Hubbard_model) with a focus on particle entanglement entropy.

The basis is enumerated using the method of [Szabados et al., 2011](http://coulson.chem.elte.hu/surjan/PREPRINTS/181.pdf).
See also [Zhang et al., 2011](http://arxiv.org/pdf/1102.4006v1.pdf).


## Requirements

* [ArgParse](https://github.com/carlobaldassi/ArgParse.jl) (`Pkg.add("ArgParse")`)
* [JeszenszkiBasis](https://github.com/0/JeszenszkiBasis.jl) (`Pkg.clone("https://github.com/0/JeszenszkiBasis.jl.git")`)

### Optional

* [LsqFit](https://github.com/JuliaOpt/LsqFit.jl) (`Pkg.add("LsqFit")`)
* [Qutilities](https://github.com/0/Qutilities.jl) (`Pkg.clone("https://github.com/0/Qutilities.jl.git")`)


## Examples

* `julia tV_main.jl --help`
* `julia tV_main.jl --out output.dat --ee 1 --site-max 1 4 2`
* `julia tV_main_neg.jl --out output.dat --ee 1 --site-max 1 4 2`



