
import os

from ytla_plan.features.feature_maker.modules.backend_python_flask.script.scriptImportAnalyzer import analyze_imports

report_path = analyze_imports(output_dir=os.getcwd())
print(f"report generated: {report_path}")
