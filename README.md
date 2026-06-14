# Heat Equation Solver

## Overview
This project is a Python implementation of a numerical solver for the 1D heat equation. It uses an Implicit Euler time discretization with a Backward Difference finite difference scheme in space, leading to a matrix-based linear solve at each time step.

The repository is a compact applied mathematics project that demonstrates finite difference modeling, linear algebra, and comparison of numerical and analytical solutions for a classical PDE.

## Mathematical Background
The 1D heat equation models how temperature evolves over time along a line segment:

```text
u_t = alpha * u_xx
```

In this project, the domain is treated on a fixed interval with interior grid points and a sinusoidal initial condition. The analytical solution for that setup is used for direct comparison and absolute error reporting.

## Numerical Method
The solver applies:
- a uniform 1D grid
- an Implicit Euler time step
- a finite difference approximation for the second spatial derivative
- a tridiagonal matrix-based system solve at every step

This corresponds to a Backward Difference style scheme in time and a standard second-order finite difference stencil in space.

## Features
- Builds a 1D spatial grid and interior points
- Computes the initial temperature vector
- Forms the finite difference coefficient matrix
- Solves the linear system at each time step with NumPy
- Evaluates the analytical solution for comparison
- Reports numerical value, analytical value, and absolute error

## Tech Stack
- Python
- NumPy

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
Run the solver:

```bash
python main.py
```

The script asks for:
- a time value `t`
- an optional position value `x`

If `x` is left blank, the program prints a table for all interior grid points. If `x` is provided, it prints the numerical solution, analytical solution, and absolute error for that location.

## Example Output
Example table header:

```text
t|x|numerik|analitik|mutlakHata
0.1|0.2|0.30025782|0.30443969|0.00418187
```

The current script compares:
- the numerical approximation
- the analytical reference solution
- the absolute error

## Project Status
This repository is a portfolio-ready cleanup of an existing educational numerical methods project. The implementation remains intentionally small and focused on the core finite difference solver.

## Future Improvements
- Refactor function names and output text into fully English terminology
- Add plotting for the numerical and analytical solution curves
- Add configurable boundary conditions and grid spacing
- Add tests for matrix assembly and error behavior
- Document stability, convergence, and discretization choices in more detail
