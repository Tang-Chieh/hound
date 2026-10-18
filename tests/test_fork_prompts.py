"""Exercise the actual prompts sent by each fork branch without model calls."""
import json

import pytest

from analysis.agent_core import AutonomousAgent
import analysis.strategist as strategist_module
from analysis.strategist import HypothesisBatchJSON, PlanBatch, Strategist


class CaptureClient:
    provider_name = 'mock'
    model = 'mock'

    def __init__(self):
        self.prompts = []

    def parse(self, *, system, user, schema, **kwargs):
        self.prompts.append(system)
        if schema is PlanBatch:
            return PlanBatch(investigations=[])
        return HypothesisBatchJSON(hypotheses=[], guidance=[])

    def raw(self, *, system, user, **kwargs):
        self.prompts.append(system)
        return json.dumps({'action': 'conclude', 'reasoning': 'No additional evidence', 'parameters': {}})


def assert_branch_scope(prompt):
    focused = hasattr(strategist_module, 'PRICE_MANIPULATION_SCOPE')
    assert ('This audit exclusively targets price manipulation vulnerabilities.' in prompt) == focused


@pytest.mark.parametrize('phase', ['Coverage', 'Saliency', None])
def test_planning_scope_without_mission(phase):
    strategist = Strategist(config={'models': {'agent': {'provider': 'mock', 'model': 'mock'}}})
    capture = CaptureClient()
    strategist.llm = capture
    strategist.plan_next(graphs_summary='Pool reads an oracle', completed=[], phase_hint=phase)
    assert capture.prompts
    assert_branch_scope(capture.prompts[0])


@pytest.mark.parametrize('phase', ['Coverage', 'Saliency'])
def test_deep_think_scope_without_mission(phase):
    strategist = Strategist(config={'models': {'agent': {'provider': 'mock', 'model': 'mock'}}})
    capture = CaptureClient()
    strategist.llm = capture
    strategist.deep_think(context='Pool collateral valuation reads reserves', phase=phase)
    assert capture.prompts
    assert_branch_scope(capture.prompts[0])


def test_scout_scope_without_mission():
    scout = AutonomousAgent.__new__(AutonomousAgent)
    capture = CaptureClient()
    scout.llm = capture
    decision = scout._get_agent_decision('Pool collateral valuation reads reserves')
    assert decision.action == 'conclude'
    assert_branch_scope(capture.prompts[0])
