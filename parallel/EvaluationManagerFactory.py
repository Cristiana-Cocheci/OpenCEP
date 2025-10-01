"""
This file contains the class responsible for evaluation manager initialization.
"""
from typing import List
from base.Pattern import Pattern
from evaluation.EvaluationMechanismFactory import EvaluationMechanismParameters
from parallel.ParallelExecutionParameters import *
from parallel.manager.SequentialEvaluationManager import SequentialEvaluationManager
from parallel.data_parallel.DataParallelEvaluationManager import DataParallelEvaluationManager
from tree.PatternMatchStorage import TreeStorageParameters


class EvaluationManagerFactory:
    """
    Creates an evaluation manager given its specification.
    """
    @staticmethod
    def create_evaluation_manager(patterns: Pattern or List[Pattern],
                                  eval_mechanism_params: EvaluationMechanismParameters,
                                  parallel_execution_params: ParallelExecutionParameters,
                                  storage_params: TreeStorageParameters):
        print("Creating evaluation manager...")
        print(f" - Parallel execution: {parallel_execution_params}\n - Storage: {storage_params}")
        if parallel_execution_params is None:
            parallel_execution_params = ParallelExecutionParameters()

        print(f" - Using {parallel_execution_params.execution_mode} execution mode")
        if parallel_execution_params.execution_mode == ParallelExecutionModes.SEQUENTIAL:
            return SequentialEvaluationManager(patterns, eval_mechanism_params, storage_params)
        if parallel_execution_params.execution_mode == ParallelExecutionModes.DATA_PARALLELISM:
            return DataParallelEvaluationManager(patterns, eval_mechanism_params, parallel_execution_params, storage_params)
        raise Exception("Unknown parallel execution mode: %s" % (parallel_execution_params.execution_mode,))
