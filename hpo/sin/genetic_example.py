#!/usr/bin/env python3
# encoding: utf-8
"""Genetic optimizer example"""
from crayai import hpo

evaluator = hpo.Evaluator('python source/sin.py', verbose=True)

params = hpo.Params([["-a", 1.0, (-1.0, 1.0)],
                     ["-b",-1.0, (-1.0, 1.0)],
                     ["-c", 1.0, (-1.0, 1.0)],
                     ["-d",-1.0, (-1.0, 1.0)],
                     ["-e", 1.0, (-1.0, 1.0)],
                     ["-f",-1.0, (-1.0, 1.0)],
                     ["-g", 1.0, (-1.0, 1.0)]])

optimizer = hpo.GeneticOptimizer(evaluator,
                                 generations=13,
                                 pop_size=10,
                                 num_demes=1,
                                 mutation_rate=0.9,
                                 log_fn='genetic.log',
                                 verbose=True)


optimizer.optimize(params)

print(optimizer.best_fom)
print(optimizer.best_params)
