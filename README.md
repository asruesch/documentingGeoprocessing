Documenting Geoprocessing Using a Scripting Language
========================

A short crash course on how to use Python scripting in lieu of metadata for documenting geoprocessing steps
------------------------

# **Why** should we use scipts for documenting our work?

1. **ALL** work is documented. Written documentation such as READMEs are great, but are only generalizations of the overall workflow. If every step was documented in the README, the process may as well be scripted!
2. The work can easily be reproduced be a **reviewer**.
3. The work can easily be reproduced by a **collaborator**.
4. The work can easily be reproduced by **you** if results need to be recalculated.
5. If well constructed (following DRY principles), scripts are modular. That is, you can write functionality to "plug into" future scripts.

# **How** we should use scripts for documenting our work

1. Annotate appropriately. Commented code helps readers interpret your calculations. For example:

```python
####################
# Calculting RUSLE #
####################

# Contributing area
Am = facLand * float(env.cellSize)**2
# Slope (in radians)
br = Slope(demFile, "DEGREE") * (math.pi / 180.0)

```
