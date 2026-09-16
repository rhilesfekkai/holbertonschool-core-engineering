#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish using multiple inheritance."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
