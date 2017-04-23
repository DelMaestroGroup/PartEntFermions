# POV-Ray Particle Partition

To generate and crop .png file:

```
povray particle_partition.pov -p +H1000 +W750 +Q11 +UA
convert particle_partition.png -crop 750x130+0+440 particle_partition.png
```

<img src="https://github.com/DelMaestroGroup/PartEntFermions/blob/master/PartitionSchematic/particle_partition.png" width=300px>

A schematic of N=7 fermions in one spatial dimension subject to
periodic boundary conditions under a n-particle partition with n=2 
(left) and anti-periodic boundary conditions with N=8 and n=3 (right).  All fermions
are identical, while the partitions A and B are distinguished via
their first quantized labels.
