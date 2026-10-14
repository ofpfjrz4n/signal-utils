"""Helpers for handling SIGTERM/SIGINT and draining work before exit."""

from __future__ import annotations

__all__ = ["signalUtils"]


def signalUtils(value):
    """Helpers for handling SIGTERM/SIGINT and draining work before exit."""
    if value is None:
        raise ValueError("value must not be None")
    return value
