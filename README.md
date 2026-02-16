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
├── core/
│   ├── aws_cli.py          # Read-only AWS CLI abstraction
│   ├── regions.py          # Multi-region execution engine
│   ├── graph.py            # Generic dependency graph model
│   ├── progress.py         # Unified progress bar manager
│   └── risk_engine.py      # Advisory-only risk classification
│
├── plugins/
│   ├── target_groups/
│   │   ├── scanner.py      # Target Group discovery
│   │   ├── checks_elb.py   # ALB/NLB references
│   │   ├── checks_ecs.py   # ECS references
│   │   ├── checks_asg.py   # Auto Scaling references
│   │   └── model.py        # TG domain model
│   └── _template/          # Plugin template for future services
│
├── reports/
│   ├── json_report.py
│   ├── markdown_report.py
│   └── html_report.py
│
├── cli.py                  # Entry point
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/rezabagheri/aws-infra-graph.git
cd aws-infra-graph
pip install -r requirements.txt
```

---

## Usage

Run a Target Group scan:

```bash
python cli.py --plugin target_groups --region us-east-1
```

Generate multiple report formats:

```bash
python cli.py --plugin target_groups --report json,markdown,html
```

---

## Output

Each run produces:

- **JSON** – machine-readable full graph
- **Markdown** – audit-friendly reports
- **HTML** – Bootstrap-styled interactive tables

All findings are **advisory only** and must be reviewed by humans before action.

---

## Roadmap

- [x] Core framework
- [x] Plugin architecture
- [x] Target Group scanner
- [x] ECS / ELB / ASG reference checks
- [x] JSON / Markdown / HTML reporting
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
