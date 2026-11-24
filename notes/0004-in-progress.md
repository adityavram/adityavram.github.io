---
title: In Progress - There's no such thing as primes
date: 2026-11-24
tags: [math, research, factoring, in-progress]
status: public
---

I'm researching whether you can tell a prime from a semiprime without factoring. You can't. Telling a prime from a semiprime is the same problem as factoring. There's no such thing as a prime number; there's a number with two divisors and a number with four divisors, and the second one is the factoring problem in disguise.

## The asymmetry

Primality testing is poly-time. AKS settles whether a single number N is prime in time polynomial in log N. Semiprime identification, deciding whether N is a product of exactly two primes, is equivalent to factoring. An oracle that computes d(N), the number of divisors of N, factors any semiprime N = pq in polynomial time: test primes m and watch whether d(N·m) is 6 or 8, and 6 means m divides N. So computing d(N) is factoring.

The gap between "is N prime?" and "is N a semiprime?" is the gap between an easy problem and a hard one. The first is cheap because a prime is the endpoint of the divisor-count spectrum: d(p) = 2, the minimum, and reaching it tells you nothing about any other number. The second is hard because d(N) = 4 for a semiprime is the next step on the spectrum, and that step is the factoring problem wearing a different face.

## Why primality is cheap

A prime is a number with exactly two divisors, 1 and itself. A semiprime N = pq has four: 1, p, q, N. The divisor count d is the whole signature. d=2 for primes, d=4 for semiprimes, d=3 for prime squares, d=6 for p²q, and so on. "Prime" is the name we gave the d=2 endpoint. It is not a separate kind of number. The identifiable category is the divisor count, and the prime is the trivial case where the answer is always "yes, d=2" once you reach it, which AKS reaches directly, without ever computing d.

The reason primality is cheap is not that primes are simple. It is that there is nothing to find. A prime has no smaller prime factor to locate; the test is "does a smaller divisor exist?" and the answer is no, full stop. A semiprime has a smaller prime factor p ≈ √N, and locating it is factoring.

## Why semiprime identification is factoring

The H12.2 direction posits that (p, q) is the unique integer point on the hyperbola xy = N with both coordinates prime. This is a genuine structural uniqueness: among the four integer points on xy = N — (1,N), (p,q), (q,p), (N,1) — exactly one has both coordinates prime. The uniqueness is real. It does not help.

The proof: given an oracle that computes d(N) for any N, you factor any semiprime N = pq. Compute d(N). If it is 4, N is a semiprime (or a prime cube, a degenerate case). Then test primes m: d(N·m) is 8 unless m divides N, in which case it is 6. A polynomial number of tests finds a factor. So any method that computes d(N) is a factoring algorithm.

The uniqueness of (p, q) on the hyperbola is an existence property. Knowing the answer is unique does not yield a method for finding it without enumeration. This is the enumeration barrier in a different guise: the structural property is real but computationally inaccessible without already factoring.

## The barrier

Every classical factoring approach requires enumeration, checking candidate divisors one by one. Trial division checks primes up to √N. Pollard's rho runs a random walk of length O(√p). CFRAC, GNFS, ECM, and lattice methods all enumerate candidate sets, just at different scales. None are polynomial.

The deeper result, from the project's key findings: every mathematical framework that encodes factor information does so symmetrically. Encoding and decoding have the same complexity. The divisor function d(N) encodes the complete prime factorization of N; computing it is decoding, and decoding is factoring. There is no framework that leaks factor information one way without also requiring it back.

The six sub-approaches of H12.2 — integer point structure, lattice point counting, Minkowski's theorem, continued fractions, primality-detecting lattices, Diophantine approximation — all hit the same wall. Either they are equivalent to factoring (computing d(N), counting points, testing primality of coordinates), or they require enumeration (CF periods are exponential, Baker bounds are too large, the hyperbolic region is nonconvex so Minkowski includes junk points). The uniqueness of (p, q) is information that requires factoring to access, not information that enables factoring.

## In progress

The open question is whether the asymmetry is real or an artifact of the frameworks we have tried. Every framework tested treats the prime as the degenerate d=2 case and the semiprime as the d=4 case, and the d=4 case reduces to factoring. The question is whether there is a framework where identifying a semiprime is cheaper than factoring, where "is N a semiprime?" is not the same question as "what are the factors of N?"

The current directions, from the project's directions file, are non-uniform algorithms (a different method per N, rather than one algorithm uniform over all semiprimes), structure in specific semiprimes (average-case factoring might be easier than worst-case, though no known structure enables poly-time factoring for even 1% of semiprimes), and the residue-tower cascade (the 2-adic filtration of identification gates, whether the free content of a semiprime accessible in poly time without factoring extends above the quadratic layer).
