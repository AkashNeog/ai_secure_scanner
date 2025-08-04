import ast
import re

# ---------- AST-Based Vulnerability Scanner ----------
class VulnerabilityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.vulnerabilities = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec']:
            self.vulnerabilities.append({
                "type": "Insecure Function Usage",
                "reason": f"Use of `{node.func.id}` is unsafe.",
                "lineno": node.lineno
            })
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and "password" in target.id.lower():
                if isinstance(node.value, ast.Str):
                    self.vulnerabilities.append({
                        "type": "Hardcoded Password",
                        "reason": "Possible hardcoded password detected.",
                        "lineno": node.lineno
                    })
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name == "pickle":
                self.vulnerabilities.append({
                    "type": "Unsafe Library Import",
                    "reason": "Pickle is unsafe for untrusted input.",
                    "lineno": node.lineno
                })

    def visit_ImportFrom(self, node):
        if node.module == "pickle":
            self.vulnerabilities.append({
                "type": "Unsafe Library Import",
                "reason": "Pickle is unsafe for untrusted input.",
                "lineno": node.lineno
            })

# ---------- NLP-Like Comment Scanner ----------
def scan_comments(code):
    comments = []
    suspicious_keywords = ["todo", "fixme", "insecure", "hack", "vulnerable", "issue", "bypass", "backdoor"]

    for lineno, line in enumerate(code.splitlines(), start=1):
        line = line.strip()
        if line.startswith("#"):
            for word in suspicious_keywords:
                if word in line.lower():
                    comments.append({
                        "comment": line,
                        "reason": f"Suspicious keyword '{word}' in comment",
                        "lineno": lineno
                    })
                    break
    return comments

# ---------- Unified Scanner Function ----------
def scan_code(code: str, filename: str = "your_file.py"):
    try:
        tree = ast.parse(code, filename=filename)
        visitor = VulnerabilityVisitor()
        visitor.visit(tree)
        vulnerabilities = visitor.vulnerabilities
    except Exception as e:
        vulnerabilities = [{"type": "Parse Error", "reason": str(e), "lineno": None}]

    comments = scan_comments(code)
    return None, comments, vulnerabilities
