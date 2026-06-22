# test_glitchpulse.py
"""
Tests for GlitchPulse module.
"""

import unittest
from glitchpulse import GlitchPulse

class TestGlitchPulse(unittest.TestCase):
    """Test cases for GlitchPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlitchPulse()
        self.assertIsInstance(instance, GlitchPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlitchPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
