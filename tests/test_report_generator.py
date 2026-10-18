"""
Tests for ReportGenerator to ensure it builds reports and calls LLM.
"""

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from analysis.report_generator import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        # Create project structure
        (self.tmp / 'graphs').mkdir()
        # Simple graph file
        (self.tmp / 'graphs' / 'graph_SystemArchitecture.json').write_text(
            json.dumps({
                'name': 'SystemArchitecture',
                'nodes': [{'id': 'n1', 'label': 'Comp', 'type': 'component'}],
                'edges': []
            })
        )
        # Hypotheses
        (self.tmp / 'hypotheses.json').write_text(json.dumps({
            'hypotheses': {
                'h1': {'title': 'test', 'vulnerability_type': 'x', 'severity': 'low', 'confidence': 0.9, 'status': 'confirmed'}
            }
        }))
        # No agent_runs required

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_generate_html_report(self):
        cfg = {'models': {'reporting': {'provider': 'openai', 'model': 'x'}}}
        with patch('analysis.report_generator.UnifiedLLMClient') as MockLLM:
            mock_llm = MagicMock()
            MockLLM.return_value = mock_llm
            mock_llm.raw.return_value = (
                '{"executive_summary": "Executive Summary Here", '
                '"system_overview": "System Overview Here"}'
            )

            rg = ReportGenerator(self.tmp, cfg)
            html = rg.generate(project_name='Proj', project_source='repo', title='Report', auditors=['A'])
            self.assertIn('Executive Summary', html)
            self.assertIn('Proj', html)
            self.assertIn('Findings', html)
            self.assertIn('System Overview', html)

    def test_suggested_mitigation_is_rendered_in_html_and_markdown(self):
        cfg = {'models': {'reporting': {'provider': 'openai', 'model': 'x'}}}
        # This test only checks deterministic formatting; do not initialize a
        # real provider or require API credentials just to render the fields.
        with patch('analysis.report_generator.UnifiedLLMClient'):
            rg = ReportGenerator(self.tmp, cfg)
        findings = [{
            'id': 'h1',
            'title': 'Manipulable spot price',
            'severity': 'high',
            'description': 'The redemption trusts current pool reserves.',
            'professional_description': 'The redemption trusts current pool reserves.',
            'affected': ['Pool.redeem'],
            'affected_description': 'Pool.redeem',
            'mitigation': 'Use a TWAP & validate the price.',
            'code_samples': [],
        }]

        html = rg._format_findings_html(findings)
        markdown = rg._format_findings_markdown(findings)

        assert 'Suggested Mitigation (not independently verified)' in html
        assert 'Use a TWAP &amp; validate the price.' in html
        assert '**Suggested Mitigation (not independently verified):** Use a TWAP & validate the price.' in markdown
