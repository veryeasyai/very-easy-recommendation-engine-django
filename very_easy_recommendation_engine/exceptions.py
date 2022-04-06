"""
Custom exceptions for Very Easy Recommendation Engine's
Django SDK.
"""


class VeryEasyRecommendationEngineException(Exception):
    """
    Base exception for VEAI exceptions.
    """


class VeryEasyRecommendationEngineMisconfiguredException(
    VeryEasyRecommendationEngineException
):
    """
    Something is misconfigured. See README.md.
    """
