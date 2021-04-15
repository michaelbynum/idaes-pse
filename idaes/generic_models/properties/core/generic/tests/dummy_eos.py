##############################################################################
# Institute for the Design of Advanced Energy Systems Process Systems
# Engineering Framework (IDAES PSE Framework) Copyright (c) 2018-2020, by the
# software owners: The Regents of the University of California, through
# Lawrence Berkeley National Laboratory,  National Technology & Engineering
# Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia
# University Research Corporation, et al. All rights reserved.
#
# Please see the files COPYRIGHT.txt and LICENSE.txt for full copyright and
# license information, respectively. Both files are also available online
# at the URL "https://github.com/IDAES/idaes-pse".
##############################################################################
"""
Mock-up EoS module for testing generic property packages
"""
from pyomo.environ import Var

from idaes.generic_models.properties.core.eos.eos_base import EoSBase


class DummyEoS(EoSBase):
    # Add attribute indicating support for electrolyte systems
    electrolyte_support = True

    def common(b, pobj):
        # Create dummy var to be returned by expression calls
        # This Var is used to create expressions where required.
        if not hasattr(b, "dummy_var"):
            b.dummy_var = Var(initialize=42)

        # Counter for how many times this method is called
        # This is used to ensure that the method has been called by checking
        # that the counter has advanced
        if hasattr(b, "eos_common"):
            b.eos_common += 1
        else:
            b.eos_common = 1

    def calculate_scaling_factors(b, pobj):
        pass

    def build_parameters(b):
        if not hasattr(b, "dummy_param"):
            b.dummy_param = Var(initialize=42)

    def dens_mass_phase(b, p):
        return 42

    def dens_mol_phase(b, p):
        return 55e3

    def enth_mol_phase(b, p):
        return 1e2*b.temperature

    def enth_mol_phase_comp(b, p, j):
        return 1e2*b.temperature

    def entr_mol_phase(b, p):
        return 42

    def entr_mol_phase_comp(b, p, j):
        return 42

    def fug_phase_comp(b, p, j):
        return 42

    def fug_coeff_phase_comp(b, p, j):
        return 42

    def gibbs_mol_phase(b, p):
        return 42

    def gibbs_mol_phase_comp(b, p, j):
        return 42
