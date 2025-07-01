# -*- coding: utf-8 -*-

from collective.ckeditortemplates.testing import CKTEMPLATES_FUNCTIONAL_TESTING
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):

    layer = CKTEMPLATES_FUNCTIONAL_TESTING

    def setUp(self):
        portal = self.layer["portal"]
        self.installer = get_installer(portal)

    def test_product_installed(self):
        """Test if collective.ckeditortemplates is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.is_product_installed("collective.ckeditortemplates"))

    def test_uninstall(self):
        """Test if collective.ckeditortemplates is cleanly uninstalled."""
        self.installer.uninstall_product("collective.ckeditortemplates")
        self.assertFalse(self.installer.is_product_installed("collective.ckeditortemplates"))
