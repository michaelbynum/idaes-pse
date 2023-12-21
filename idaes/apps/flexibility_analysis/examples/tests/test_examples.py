from idaes.apps.flexibility_analysis import _check_dependencies, _check_relu_dependencies
import idaes.apps.flexibility_analysis as flex
from idaes.apps.flexibility_analysis.examples import linear_hx_network, nonlin_hx_network, idaes_hx_network
import unittest
import pytest


@pytest.mark.unit
class TestExamples(unittest.TestCase):
    def test_linear_hx_network(self):
        res = linear_hx_network.main(flex_index=False, method=flex.FlexTestMethod.active_constraint, plot_history=False)
        self.assertEqual(res.termination, flex.FlexTestTermination.found_infeasible_point)
        self.assertAlmostEqual(res.max_constraint_violation, 4, 5)

        res = linear_hx_network.main(flex_index=False, method=flex.FlexTestMethod.vertex_enumeration, plot_history=False)
        self.assertEqual(res.termination, flex.FlexTestTermination.found_infeasible_point)
        self.assertAlmostEqual(res.max_constraint_violation, 8.8, 5)

        res = linear_hx_network.main(flex_index=False, method=flex.FlexTestMethod.linear_decision_rule, plot_history=False)
        self.assertEqual(res.termination, flex.FlexTestTermination.found_infeasible_point)

        res = linear_hx_network.main(flex_index=False, method=flex.FlexTestMethod.relu_decision_rule, plot_history=False)
        self.assertEqual(res.termination, flex.FlexTestTermination.found_infeasible_point)

        res = linear_hx_network.main(flex_index=True, method=flex.FlexTestMethod.active_constraint, plot_history=False)
        self.assertAlmostEqual(res, 0.5, 5)

        res = linear_hx_network.main(flex_index=True, method=flex.FlexTestMethod.vertex_enumeration, plot_history=False)
        self.assertAlmostEqual(res, 0.5, 5)

        res = linear_hx_network.main(flex_index=True, method=flex.FlexTestMethod.linear_decision_rule, plot_history=False)
        self.assertLessEqual(res, 0.5)

        res = linear_hx_network.main(flex_index=True, method=flex.FlexTestMethod.relu_decision_rule, plot_history=False)
        self.assertAlmostEqual(res, 0.5, 2)

    def test_idaes_hx_network(self):
        res = idaes_hx_network.main(flex.FlexTestMethod.sampling)
        self.assertEqual(res.termination, flex.FlexTestTermination.found_infeasible_point)
        self.assertAlmostEqual(res.max_constraint_violation, 0.375170890924453)  # regression