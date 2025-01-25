import logging

from app.components.knapsack.service import KnapsackSolverService


class Dependencies:
    """
    Class: Dependencies

    """

    _knapsack_solver_service: KnapsackSolverService()

    # _database_manager: DatabaseManager
    # _cache_manager: CacheManager

    @classmethod
    def start(cls):
        logging.info("Starting dependencies...")
        cls._knapsack_solver_service = KnapsackSolverService()

    @classmethod
    def stop(cls):
        logging.info("Stopping dependencies...")

    """
    @classmethod
    def cache_manager(cls) -> CacheManager:
        return cls._cache_manager

    @classmethod
    def db_manager(cls) -> DatabaseManager:
        return cls._database_manager
    """

    @classmethod
    def knapsack_solver_service(cls) -> KnapsackSolverService:
        return cls._knapsack_solver_service
