# SECTION 9: Firewall Rules

## 1️⃣ Plain-English Explanation
You have a house (VM) on a street (Subnet). You have a fence around the house.
The **Firewall Rule** is the Security Guard at the gate.
*   **Ingress (Incoming):** People trying to enter your house. (Default: **BLOCKED**).
*   **Egress (Outgoing):** You leaving your house to go to the store. (Default: **ALLOWED**).

## 2️⃣ Critical Logic: Priority & Statefulness
### Rules of the Game
1.  **Implied Deny Ingress**: If you don't explicitly allow it, nobody gets in.
2.  **Implied Allow Egress**: Your server can talk to the internet (download updates) unless you block it.
3.  **Stateful Nature**: If you allow a request OUT, the reply is automatically allowed IN. You do NOT need a "return traffic" rule.

### Priority System
*   Range: `0` (Highest) to `65535` (Lowest).
*   **Logic**: The first rule that matches wins.
*   *Example:*
    *   Rule A (Priority 1000): **Deny** All from IP `1.2.3.4`.
    *   Rule B (Priority 65535): **Allow** All.
    *   *Result:* IP `1.2.3.4` is blocked.

## 3️⃣ Visual Guide: The Filter Process
```mermaid
graph TD
    Traffic[Incoming Traffic] --> Priority1[Check Priority 0-999]
    Priority1 -- No Match --> Priority2[Check Priority 1000]
    Priority2 -- Match Found (Allow) --> Allow[✅ Traffic Allowed]
    Priority2 -- Match Found (Deny) --> Deny[❌ Traffic Blocked]
    Priority2 -- No Match --> Default[Check Implied Rules]
    Default --> Blocked[🚫 Blocked (Implied Deny)]
    
    style Allow fill:#dcfce7,stroke:#15803d
    style Deny fill:#fee2e2,stroke:#991b1b
    style Blocked fill:#f3f4f6,stroke:#6b7280
```

## 4️⃣ Tags & Service Accounts (The Pro Move) 🏆
Instead of saying "IP 10.0.0.5 can talk to IP 10.0.0.6", we use **Identities**.

### Bad Way (IP-Based)
*   "Allow `10.128.0.5` to reach Port 80."
*   *Why it fails:* If you delete the VM and create a new one, it gets a new IP. The rule breaks.

### Good Way (Tags)
*   **Tag:** sticky note on a VM (e.g., `web-server`, `frontend`).
*   **Rule:** "Allow source tag `frontend` to reach target tag `backend`."
*   *Why it works:* It scales automatically.

### Best Way (Service Accounts)
*   **Identity:** Cryptographic identity of the VM.
*   **Rule:** "Allow SA `web-app@...` to reach SA `database@...`."
*   *Why it's best:* Tags can be modified by anyone with "Instance Edit" graphics. Service Accounts require IAM Admin capability. More secure.

## 5️⃣ Real-World Scenarios (Zero-to-Hero) ⚡

### Scenario A: The "Just in Time" SSH
*   **Don't:** Open Port 22 to `0.0.0.0/0` (The World). You will get hacked in minutes.
*   **Do:** Open Port 22 to `35.235.240.0/20` (Identity-Aware Proxy).
*   *Benefit:* You SSH via the browser console without exposing the VM to the public internet check `tunnel-through-iap`.

### Scenario B: Logging
*   **Problem:** "My app can't connect to the database!"
*   **Fix:** Turn on **Firewall Rule Logging**.
*   *Inspect:* Go to Cloud Logging. Search `jsonPayload.rule_details`. See if the packet was ALLOWED or DENIED.

## 6️⃣ Hands-On: Console Walkthrough
1.  **Go to:** VPC Network > Firewall.
2.  **Click:** Create Firewall Rule.
3.  **Name:** `allow-web-ingress`.
4.  **Direction:** Ingress.
5.  **Targets:** "Specified target tags".
6.  **Target Tags:** `web-server`.
7.  **Source Filter:** IPv4 ranges (`0.0.0.0/0` for "Everyone").
8.  **Protocols/Ports:** tcp: `80`, `443`.
9.  **Result:** Any VM tagged `web-server` helps serve traffic.

## 7️⃣ Checkpoint Questions (Exam Style)
**Q1. A junior engineer creates a rule with Priority 1000 to ALLOW port 80. You create a rule with Priority 100 to DENY port 80. What happens?**
*   A. Traffic is Allowed.
*   B. Traffic is Denied.
*   C. Both rules conflict and error out.
*   D. Traffic is allowed only if authenticated.
> **Answer: B.** Lower priority number (100) wins.

**Q2. You want to allow SSH access ONLY from Google's Cloud Console (IAP). Which source range do you use?**
*   A. `0.0.0.0/0`
*   B. `10.0.0.0/8`
*   C. `35.235.240.0/20`
*   D. `192.168.1.1/32`
> **Answer: C.** This is the IAP (Identity-Aware Proxy) forwarding range.

**Q3. Which firewall target is the most secure against internal "spoofing" or accidental tag changes?**
*   A. Network Tags
*   B. Service Accounts
*   C. Zone Targets
*   D. IP Ranges
> **Answer: B.** Service Accounts are strictly controlled via IAM, whereas Tags are mutable properties of the instance.

**Q4. True or False: Firewall rules are Regional resources.**
*   A. True
*   B. False (They are Global)
*   C. False (They are Zonal)
> **Answer: B.** VPC Firewall rules are **Global** resources. They act across the entire VPC, though you can filter by target tags.


<!-- FLASHCARDS
[
  {
    "term": "Ingress",
    "def": "Incoming traffic (Example: User visiting your website)."
  },
  {
    "term": "Egress",
    "def": "Outgoing traffic (Example: VM downloading an update)."
  },
  {
    "term": "Priority",
    "def": "Lower number beats Higher number (0-65535). 1000 overrides 65535."
  },
  {
    "term": "Implied Deny",
    "def": "By default, all Ingress is BLOCKED."
  },
  {
    "term": "Network Tag",
    "def": "Label attached to a VM to apply firewall rules (e.g., 'web-server')."
  }
]
-->
