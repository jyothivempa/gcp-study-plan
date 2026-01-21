# How GCP Interviews Are Run

> **Insider Guide:** What to expect and how to prepare for each interview round.

---

## 📋 Interview Round Structure

Most GCP/Cloud Engineer interviews follow this structure:

| Round | Duration | Focus | Weight |
|-------|----------|-------|--------|
| **Phone Screen** | 30-45 min | Resume, basics, motivation | 20% |
| **Technical Deep-Dive** | 45-60 min | Core concepts, troubleshooting | 30% |
| **System Design** | 45-60 min | Architecture, trade-offs | 30% |
| **Behavioral** | 30-45 min | Teamwork, conflict, growth | 20% |

---

## 📞 Round 1: Phone Screen

### What to Expect
- Recruiter or hiring manager
- High-level technical questions
- "Tell me about yourself"
- Why this company/role?

### Sample Questions
- "Walk me through a GCP project you've worked on"
- "What's the difference between Cloud Run and GKE?"
- "How would you explain VPC to a non-technical person?"

### Success Pattern
```
✅ 30-second intro, then ask "Should I go deeper?"
✅ Connect your experience to the job description
✅ Show enthusiasm for cloud, not just "I need a job"
```

---

## 🔧 Round 2: Technical Deep-Dive

### What to Expect
- Senior engineer or team lead
- Troubleshooting scenarios
- "You did X, but what if Y happened?"
- Live debugging (sometimes)

### Question Categories

| Category | % of Questions | Example |
|----------|----------------|---------|
| **Conceptual** | 30% | "What is Workload Identity?" |
| **Trade-off** | 30% | "When Cloud SQL vs Spanner?" |
| **Troubleshooting** | 40% | "VM can't reach internet. Debug this." |

### Troubleshooting Framework (Use This!)

```
1. CLARIFY the symptom
   → "Can you describe the exact error?"

2. ISOLATE the layer
   → Network? IAM? Application? Configuration?

3. LIST possible causes
   → "This could be firewall, route, or IAM..."

4. VERIFY methodically
   → "I'd run `gcloud compute instances describe...`"

5. FIX and VALIDATE
   → "After fixing, I'd test with `curl` and check logs"
```

### Sample Deep-Dive Questions

**IAM:**
> "Developer says 'Permission Denied' when deploying to Cloud Run. Walk me through your debugging."

**Strong Answer:**
```
1. Check identity: `gcloud auth list`
2. Check project: `gcloud config list project`
3. Check role: needs `roles/run.developer` or `roles/run.admin`
4. Check if org policy blocks public services
5. Test: `gcloud projects get-iam-policy PROJECT_ID`
```

**Networking:**
> "VM in private subnet can't pull Docker images. Debug this."

**Strong Answer:**
```
1. No external IP? → Need Cloud NAT or Private Google Access
2. Check route to 0.0.0.0/0 through NAT
3. Check firewall allows egress on 443
4. For gcr.io: Enable Private Google Access on subnet
5. Test: `curl -v https://gcr.io`
```

---

## 🏗️ Round 3: System Design

### What to Expect
- Whiteboard or virtual diagram
- Open-ended requirements
- "Design a system that..."
- Trade-off discussions

### The 5-Step Framework

```
1. CLARIFY requirements (2-3 min)
   → Users? Scale? Latency? Budget? Compliance?

2. HIGH-LEVEL design (5 min)
   → Draw boxes: User → LB → App → DB

3. DEEP-DIVE components (15 min)
   → Pick 2-3 areas to detail

4. TRADE-OFFS (10 min)
   → "I chose X over Y because..."

5. FUTURE improvements (5 min)
   → "To scale further, I'd add..."
```

### Sample Design Questions

| Question | Key Services | Watch For |
|----------|-------------|-----------|
| "Design a web app with 99.9% uptime" | Regional MIG, GLB, Cloud SQL HA | Auto-healing, multi-zone |
| "Design a data pipeline for 1M events/day" | Pub/Sub, Dataflow, BigQuery | DLQ, partitioning, costs |
| "Design a CI/CD pipeline" | Cloud Build, Artifact Registry, GKE | Security, rollback, testing |

### Design Answer Template

```markdown
## Requirements I'm Assuming
- X users, Y requests/second
- 99.9% availability target
- Budget: cost-optimized

## Architecture
[Draw diagram]
- Users → Cloud CDN → Global LB
- LB → Regional MIG (3 zones)
- App → Cloud SQL (HA replica)
- Secrets → Secret Manager

## Why These Choices
| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
| Regional MIG | Zone failure tolerance | Zonal (cheaper but risky) |
| Cloud SQL HA | Built-in failover | Self-managed Postgres (more work) |

## Trade-offs
- Higher cost for HA vs single-zone
- More complexity for reliability

## Future Improvements
- Add Cloud Armor for DDoS
- Move to GKE for microservices
```

---

## 🤝 Round 4: Behavioral

### What to Expect
- STAR format (Situation, Task, Action, Result)
- Focus on collaboration and conflict
- Growth mindset signals

### Common Questions

| Question | What They're Testing |
|----------|----------------------|
| "Tell me about a production outage" | Calm under pressure, learning |
| "Disagreement with a teammate" | Conflict resolution |
| "Mistake you made and learned from" | Accountability |
| "Project you're proud of" | Impact, ownership |

### STAR Answer Template

```
SITUATION: "We had a production database failure during peak traffic..."

TASK: "I was the on-call engineer responsible for restoring service..."

ACTION: "I first checked Cloud Monitoring, then..."
- Specific technical steps
- Collaboration with team
- Communication to stakeholders

RESULT: "Service was restored in 45 minutes, and we..."
- Quantify impact
- What you learned
- Process improvement made
```

---

## 💡 Interview Tips by Role

### 🔍 Cloud Engineer Lens
| Focus On | De-emphasize |
|----------|--------------|
| Infrastructure: VM, VPC, IAM | Complex data pipelines |
| Troubleshooting skills | ML/AI services |
| Cost optimization | Deep Kubernetes internals |

### 🔍 DevOps Engineer Lens
| Focus On | De-emphasize |
|----------|--------------|
| CI/CD pipelines | Data warehousing |
| Terraform, automation | BigQuery optimization |
| Container deployment | Network design |

### 🔍 Data Engineer Lens
| Focus On | De-emphasize |
|----------|--------------|
| BigQuery, Dataflow, Pub/Sub | VM troubleshooting |
| Data modeling, ETL | Firewall rules |
| Cost optimization for data | Compute pricing |

---

## ✅ Pre-Interview Checklist

### 1 Week Before
- [ ] Review all 18 enhanced modules
- [ ] Complete 3+ mini-projects
- [ ] Practice 10 interview questions out loud

### Day Before
- [ ] Review your resume projects in detail
- [ ] Prepare 3 STAR stories
- [ ] Get a good night's sleep

### 1 Hour Before
- [ ] Have water ready
- [ ] Test video/audio
- [ ] Have pen and paper for notes

### During Interview
- [ ] Ask clarifying questions
- [ ] Think out loud
- [ ] Admit what you don't know, then explain your approach
- [ ] Relate answers to real experience when possible

---

## 🚫 Red Flags to Avoid

| Don't Say | Why It's Bad | Say Instead |
|-----------|--------------|-------------|
| "I've never used that" | Shuts down conversation | "I haven't used X, but based on my understanding..." |
| "That's easy" | Sounds arrogant | "I've done something similar..." |
| "I don't know" (alone) | No effort shown | "I'd approach it by first checking..." |
| "We did it" (always) | No individual contribution | "My role was..." then "The team also..." |
