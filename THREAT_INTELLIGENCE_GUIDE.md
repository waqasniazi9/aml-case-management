# Cybersecurity Threat Intelligence Integration Guide

## Overview

The FIA AML Case Management System v3.5+ now includes **Cybersecurity Threat Intelligence** capabilities powered by weekly research summaries. This enables the system to track supply chain attacks, malware campaigns, APTs, and other threats while linking them to active AML investigations.

## Features

### Threat Ingestion

- ✅ Import threats from weekly research summaries
- ✅ Automatic categorization (Supply Chain, Malware, APT, Data Breach, etc.)
- ✅ Severity assessment (Info, Low, Medium, High, Critical)
- ✅ Multiple indicator types (IoC, Hash, IP, Domain, URL, Package, CVE, Wallet)

### Threat Analysis

- ✅ Search threats by title, category, or affected packages
- ✅ Store and track Indicators of Compromise (IoCs)
- ✅ Link threats to AML cases
- ✅ Check wallet addresses against threat databases
- ✅ Generate threat intelligence summaries

### Risk Assessment

- ✅ Confidence scoring for indicators (0-100)
- ✅ Pattern detection across threats
- ✅ Case-threat association tracking
- ✅ Automated threat dashboarding

## Database Tables

### cybersecurity_threats

```
id              - Unique threat identifier
title           - Threat name/title
description     - Detailed threat description
category        - Threat category (SUPPLY_CHAIN, MALWARE, APT, etc.)
severity        - Severity level (CRITICAL, HIGH, MEDIUM, LOW, INFO)
affected_systems - List of affected systems/applications
source          - Information source (e.g., "Weekly Research")
discovered_date - When threat was discovered
recommendations - Security recommendations
related_packages - Affected software packages
attack_vector   - Attack method/vector
created_at      - Ingestion timestamp
updated_at      - Last update timestamp
```

### threat_indicators

```
id              - Unique indicator ID
indicator       - The actual indicator (hash, IP, domain, etc.)
indicator_type  - Type of indicator (IOC, MALWARE_HASH, IP_ADDRESS, etc.)
threat_id       - Links to cybersecurity_threats
confidence_score - Confidence level (0-100)
first_seen      - When indicator was first observed
last_seen       - Last time indicator was observed
is_confirmed    - Whether indicator is confirmed/validated
related_threats - Other threats using same indicator
```

### threat_case_associations

```
id              - Association ID
threat_id       - Links to cybersecurity_threats
case_id         - Links to AML cases
association_type - Type of association (related, sourced_from, etc.)
confidence      - Confidence of association (low, medium, high)
notes           - Additional notes about association
created_at      - When association was created
```

## API Endpoints

### Threat Ingestion

#### Ingest New Threat

```http
POST /api/threats/ingest
Content-Type: application/json

{
    "title": "Shai-Hulud Worm Returns (v2)",
    "description": "Self-replicating npm worm affecting 800+ packages",
    "category": "supply_chain",
    "severity": "critical",
    "affected_systems": ["npm", "Maven", "GitHub"],
    "indicators": ["bcryptjs-node", "cross-sessions", "json-oauth"],
    "indicator_type": "package_name",
    "source": "Weekly Research",
    "discovered_date": "2025-12-02",
    "recommendations": [
        "Audit npm dependencies immediately",
        "Check for compromised packages",
        "Implement software supply chain verification"
    ],
    "related_packages": ["npm", "Maven ecosystem"],
    "attack_vector": "Preinstall scripts for credential theft"
}
```

**Response (201):**

```json
{
    "success": true,
    "message": "Threat ingested successfully",
    "threat_id": "threat-uuid-123"
}
```

### Threat Search & Retrieval

#### Search Threats

```http
GET /api/threats/search?q=shai-hulud&type=title
```

**Response (200):**

```json
{
    "success": true,
    "query": "shai-hulud",
    "type": "title",
    "results": [
        {
            "id": "threat-uuid",
            "title": "Shai-Hulud Worm Returns (v2)",
            "category": "supply_chain",
            "severity": "critical",
            "source": "Weekly Research"
        }
    ],
    "count": 1
}
```

#### Get Threat Details

```http
GET /api/threats/{threat_id}
```

**Response (200):**

```json
{
    "success": true,
    "threat": {
        "id": "threat-uuid",
        "title": "Shai-Hulud Worm Returns (v2)",
        "description": "Self-replicating npm worm...",
        "category": "supply_chain",
        "severity": "critical",
        "affected_systems": ["npm", "Maven", "GitHub"],
        "source": "Weekly Research",
        "discovered_date": "2025-12-02",
        "recommendations": [...],
        "related_packages": [...],
        "attack_vector": "Preinstall scripts",
        "created_at": "2025-12-02T10:30:00"
    }
}
```

### Threat-Case Linking

#### Link Threat to Case

```http
POST /api/threats/{threat_id}/link
Content-Type: application/json

{
    "case_id": "case-uuid-123",
    "association_type": "related"
}
```

**Response (200):**

```json
{
    "success": true,
    "message": "Threat linked to case successfully"
}
```

### Threat Indicator Checking

#### Check Case Wallets Against Threats

```http
POST /api/threats/indicators/check
Content-Type: application/json

{
    "case_id": "case-uuid-123"
}
```

**Response (200):**

```json
{
    "success": true,
    "matches": {
        "case_id": "case-uuid-123",
        "total_wallets": 2,
        "threats_detected": [
            {
                "wallet": "wallet-address-123",
                "threat_id": "threat-uuid",
                "threat_title": "OtterCookie Malware Campaign",
                "severity": "critical",
                "category": "malware"
            }
        ],
        "high_risk_count": 1
    }
}
```

### Threat Intelligence Dashboards

#### Get Threats Summary

```http
GET /api/threats/summary
```

**Response (200):**

```json
{
    "success": true,
    "summary": {
        "total_threats": 42,
        "threats_by_severity": {
            "critical": 8,
            "high": 15,
            "medium": 12,
            "low": 7
        },
        "threats_by_category": {
            "supply_chain": 12,
            "malware": 18,
            "apt": 7,
            "data_breach": 5
        },
        "total_indicators": 156,
        "high_confidence_indicators": 132
    }
}
```

#### Get Threats Dashboard

```http
GET /api/threats/dashboard
```

**Response (200):**

```json
{
    "success": true,
    "dashboard": {
        "total_threats": 42,
        "critical_threats": 8,
        "high_threats": 15,
        "medium_threats": 12,
        "total_indicators": 156,
        "high_confidence_indicators": 132,
        "threats_by_category": {
            "supply_chain": 12,
            "malware": 18,
            "apt": 7,
            "data_breach": 5
        }
    }
}
```

## Threat Categories

```
SUPPLY_CHAIN     - npm worms, package compromises, dependency attacks
MALWARE          - Trojans, worms, spyware, ransomware variants
APT              - Advanced Persistent Threat campaigns
DATA_BREACH      - Unauthorized data access/exfiltration
VULNERABILITY    - CVEs, unpatched systems, exploitable flaws
RANSOMWARE       - Ransomware campaigns and variants
SOCIAL_ENGINEERING - Phishing, pretexting, impersonation attacks
CRYPTO_FRAUD     - Cryptocurrency-related scams and attacks
```

## Severity Levels

```
CRITICAL         - Immediate action required, widespread impact
HIGH             - Urgent attention needed, significant risk
MEDIUM           - Requires monitoring and planning
LOW              - Informational, low immediate impact
INFO             - General security information
```

## Integration Workflow

### 1. Ingest Weekly Threats

```bash
POST /api/threats/ingest
{
    "title": "Weekly Research Summary - Week X",
    "category": "supply_chain",
    "severity": "critical",
    "indicators": [...]
}
```

### 2. Link to Active Cases

```bash
POST /api/threats/{threat_id}/link
{
    "case_id": "case-uuid",
    "association_type": "related"
}
```

### 3. Check Case Wallets

```bash
POST /api/threats/indicators/check
{
    "case_id": "case-uuid"
}
```

### 4. Monitor Dashboard

```bash
GET /api/threats/dashboard
```

## Example: Supply Chain Attack Investigation

### Scenario

Weekly research identifies compromised npm package affecting your suspect's wallet service.

### Steps

**1. Ingest the Threat**

```bash
curl -X POST http://localhost:5000/api/threats/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "title": "OtterCookie Malware in npm",
    "description": "197 malicious npm packages deployed by NK threat actors",
    "category": "supply_chain",
    "severity": "critical",
    "affected_systems": ["npm", "node-js applications"],
    "indicators": ["bcryptjs-node", "cross-sessions", "json-oauth"],
    "indicator_type": "package_name",
    "source": "Weekly Research",
    "recommendations": [
      "Audit dependencies for malicious packages",
      "Check deployment logs",
      "Verify wallet security"
    ]
  }'
```

**2. Link to AML Case**

```bash
curl -X POST http://localhost:5000/api/threats/{threat_id}/link \
  -H "Content-Type: application/json" \
  -d '{
    "case_id": "case-uuid-123",
    "association_type": "related"
  }'
```

**3. Check Associated Wallets**

```bash
curl -X POST http://localhost:5000/api/threats/indicators/check \
  -H "Content-Type: application/json" \
  -d '{
    "case_id": "case-uuid-123"
  }'
```

**4. View Results**

```
Results show wallet was registered with service using compromised package
→ Potential compromise of wallet keys
→ Elevated risk assessment
→ Additional investigation warranted
```

## Threat Data Sources

### Primary Source: Weekly Research

- **URL:** <https://github.com/Masakore/gh-weekly-research>
- **Update Frequency:** Weekly
- **Coverage:**
  - Supply Chain Attacks
  - Malware Campaigns
  - APT Activities
  - Vulnerability Disclosures
  - Government Actions
  - Third-Party Risks

### Data Includes

- Threat titles and descriptions
- Affected systems and packages
- Threat indicators (hashes, domains, IPs)
- Attack vectors and methods
- Security recommendations
- Related threat actors

## Security Recommendations

### For AML Investigators

1. **Monitor Threat Feeds** - Check new threats weekly
2. **Link Related Cases** - Connect threats to investigations
3. **Check Wallets** - Verify suspect wallets against threat IoCs
4. **Track Patterns** - Identify connection between threats and cases
5. **Document Associations** - Maintain audit trail of threat-case links

### For System Administrators

1. **Maintain IoC Database** - Keep threat indicators current
2. **Monitor Dashboard** - Track critical threats
3. **Search Capabilities** - Enable quick threat lookups
4. **Case Linking** - Document threat-case relationships
5. **Audit Logging** - Track all threat operations

## API Summary

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/threats/ingest` | POST | Add new threat |
| `/api/threats/search` | GET | Search threats |
| `/api/threats/{id}` | GET | Get threat details |
| `/api/threats/{id}/link` | POST | Link to case |
| `/api/threats/indicators/check` | POST | Check wallets |
| `/api/threats/summary` | GET | Get statistics |
| `/api/threats/dashboard` | GET | View dashboard |

## Integration with Solana ACL

- ✅ Check wallet addresses against threat indicators
- ✅ Link Solana wallets to threat cases
- ✅ Assess crypto transaction risk based on threats
- ✅ Track wallets associated with compromised packages
- ✅ Monitor for supply chain compromises in crypto infrastructure

## Version Information

- **System Version:** 3.5+
- **Threat Intelligence Module:** 1.0
- **Database Version:** 8 tables (with threat tables)
- **API Endpoints:** 8 threat-specific endpoints
- **Data Source:** Weekly Cybersecurity Research

## Support & Documentation

For more information:

- See [README_v3.5.md](README_v3.5.md) for system overview
- See [SOLANA_ACL_INTEGRATION.md](SOLANA_ACL_INTEGRATION.md) for wallet features
- Check code comments in `aml_system.py` for implementation details
