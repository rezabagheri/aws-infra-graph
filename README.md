# AWS Infra Graph

**A dynamic, plugin-based AWS infrastructure analysis and dependency graph framework.**

---

## Overview

`aws-infra-graph` is a **read-only, production-safe AWS auditing framework** designed to analyze and model relationships between AWS resources.

The project aims to build a **complete infrastructure dependency graph** across AWS services such as:

- Application / Network Load Balancers
- Target Groups
- ECS (Clusters, Services, Tasks)
- EC2
- Auto Scaling Groups
- Security Groups
- Route53
- and more

The system is **plugin-based**, enabling independent scanners to be added incrementally without modifying the core engine.

---

## Design Principles

- **Read-only by design** – no AWS resource is modified or deleted
- **Zero hardcoded values** – fully dynamic discovery
- **Production-safe** – suitable for live AWS environments
- **Plugin architecture** – each AWS domain is isolated
- **Graph-oriented output** – future-ready for visualization
- **Multi-format reporting** – JSON, Markdown, HTML

---

## Project Structure

```
aws-infra-graph/
│
├── aws_infra_graph/
│   ├── aws/                # AWS session & base modules
│   ├── cli/                # CLI entrypoint
│   ├── core/               # Graph, node, edge core models
│   ├── output/             # JSON & Mermaid output generators
│   └── plugins/            # Plugin registry & implementations
│
├── tests/                  # Unit and integration tests
├── pyproject.toml          # Modern Python packaging & dependencies
├── README.md
└── LICENSE
```

---

## Installation

Using `pyproject.toml` and editable install:

```
git clone https://github.com/rezabagheri/aws-infra-graph.git
cd aws-infra-graph
python -m venv venv
source venv/bin/activate
pip install -e .
```

> ✅ Verified on macOS with Python 3.12.5 and OpenSSL 3.6.1; scan runs without hash warnings.

---

## Usage

Run a Target Group scan:

```
aws-infra-graph scan --plugin target_groups --region us-east-1
```

Generate multiple report formats:

```
aws-infra-graph scan --plugin target_groups --report json,mermaid
```

---

## Output

Each run produces:

- **JSON** – machine-readable full graph
- **Mermaid** – visual dependency graph for Markdown
- **Markdown / HTML** – audit-friendly interactive reports

All findings are **advisory only** and must be reviewed by humans before action.

---

## Roadmap

- [x] Core framework
- [x] Plugin architecture
- [x] Target Group scanner
- [x] ECS / ELB / ASG reference checks
- [x] JSON / Mermaid / Markdown reporting
- [ ] CloudWatch signal correlation
- [ ] ALB plugin
- [ ] ECS plugin
- [ ] EC2 plugin
- [ ] Security Group plugin
- [ ] Route53 plugin
- [ ] Multi-account support
- [ ] Graph visualization (DAG)

---

## Author

**Reza Bagheri**
Email: rezabagheri@gmail.com
GitHub: https://github.com/rezabagheri
Company: Paradisecyber (https://paradisecyber.com)

---

## License

Licensed under the **Apache License, Version 2.0**.
See the `LICENSE` file for full details.
