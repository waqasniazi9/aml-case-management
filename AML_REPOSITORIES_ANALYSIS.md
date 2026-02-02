# Comprehensive Analysis of 6 AML GitHub Repositories

**Generated:** February 1, 2026

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Detailed Analysis by Repository](#detailed-analysis-by-repository)
3. [Comparative Analysis](#comparative-analysis)
4. [Integration Recommendations](#integration-recommendations)
5. [Technical Implementation Guide](#technical-implementation-guide)

---

## Repository Overview

| Repository | Stars | Focus Area | Primary Tech | Maturity |
|-----------|-------|-----------|-------------|----------|
| Jube | 49 | Real-time transaction monitoring & case management | C#/.NET | Mature |
| AMLSim | 334 | Transaction simulation & synthetic data generation | Java/Python | Stable |
| AML-Data | 68 | Synthetic transaction dataset | CSV-based | Stable |
| aml-mcp | 3 | Blockchain/crypto AML screening | Python/MCP | Recent |
| Anti-Money-Laundering-Project | 8 | Transaction analysis & visualization | Python/Jupyter | Academic |
| Databricks AML | 4 | Enterprise-scale analytics on Lakehouse | PySpark | Production |

---

## Detailed Analysis by Repository

### 1. Jube - AML Fraud Transaction Monitoring

**Repository:** <https://github.com/jube-home/aml-fraud-transaction-monitoring>

#### Main Purpose and Focus

- **Primary Goal:** Open-source real-time AML and fraud detection platform for transaction monitoring
- **Target Users:** Compliance teams, financial institutions, fintechs
- **Key Differentiator:** Fully transparent, auditable, no vendor lock-in (AGPLv3)
- **Unique Value:** Combines ML, rules-based detection, and workflow-driven case management in single system

#### Key Features and Capabilities

**Real-Time Transaction Monitoring:**

- Stateless, horizontally scalable architecture
- Low-latency, in-memory processing using Redis
- Frequently accessed immutable state cached locally
- Durable storage via PostgreSQL
- AMQP integration (RabbitMQ) for event streaming
- Support for sync/async/hybrid HTTP, AMQP interfaces
- Real-time reprocessing of historical data

**Adaptive Machine Learning (Exhaustive Adaptation):**

- Unsupervised learning for anomaly detection (deviations from normal behavior)
- Supervised learning for known fraud/AML patterns
- Hybrid supervised-unsupervised approach
- "Exhaustive Adaptation" - evolves model topology by testing different neural network structures
- Behavioral feature abstraction (transaction volume, velocity, geolocation)
- Interpretable and actionable risk insights
- Continuous model retraining on new data patterns

**Flexible Rule Engine:**

- Threshold-based detection
- Velocity checks and aggregation counts
- Automated sanctions list screening (integrated with ML)
- Time-to-live (TTL) counters and suppression rules
- Online/background velocity preparation options
- Fully integrates with ML outputs

**Workflow-Driven Case Management:**

- Multiple case streams (AML, fraud, compliance)
- Dashboard-based investigation workflows
- Document management (EDD, CDD, ID verification)
- Automatic case escalation via activation rules
- Full audit trails for all actions
- Document versioning and upload

**Cloud-Native Architecture:**

- Docker & Kubernetes support
- Multi-tenancy capability (independent rules/workflows per tenant)
- Configuration preservation (backup/restore/migration)
- High-performance caching for low-latency decisioning

#### Data Models and Schemas

**Core Entity Models:**

```
- Accounts: account_id, account_name, entity_type, risk_level, status
- Transactions: transaction_id, originator, beneficiary, amount, timestamp, type, flags
- Alerts: alert_id, account_id, alert_type, severity, timestamp, resolution_status
- Cases: case_id, account_id, case_status, documents[], escalation_rules, audit_log
- Rules: rule_id, rule_type, parameters[], threshold, time_window, action
- Sanctions: entity_id, sanctions_list, match_confidence, update_timestamp
```

**State Management:**

- Redis: Mutable state (velocity counters, transaction buffers)
- PostgreSQL: Immutable state (transaction history, audit logs)
- Local Cache: Frequently accessed reference data (sanctions lists, rule definitions)

#### Detection/Monitoring Algorithms

**Anomaly Detection (Unsupervised):**

- Statistical deviation analysis
- Behavioral baseline establishment
- Real-time comparison with learned patterns
- Support vector machines (SVM) for boundary detection

**Risk Scoring (Supervised & Unsupervised):**

- Neural network models with adaptive topology
- Decision Trees (ID3, C4.5) for interpretability
- Random Forest ensemble methods
- Hidden Markov Models for sequential patterns
- Support Vector Machines for classification

**Rule-Based Detection:**

- Threshold crossings (amount, frequency, velocity)
- Aggregation analysis (cumulative amounts over time windows)
- Pattern matching (cyclical transactions, round-tripping)
- Velocity checks (transactions per hour/day)
- Geographic anomalies
- Counterparty analysis

**Integration with Sanctions Screening:**

- Automated checks against OFAC, UN, EU sanctions lists
- Fuzzy matching for name variations
- Integration with ML risk scores for combined scoring

#### Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | C# .NET 9+ |
| Real-time Processing | Redis (in-memory) |
| Persistent Storage | PostgreSQL |
| Message Queue | RabbitMQ (AMQP) |
| API | RESTful HTTP, AMQP |
| Frontend | HTML5, CSS3, JavaScript |
| ML Framework | Accord.NET (neural networks, decision trees, random forests) |
| Deployment | Docker, Docker Compose, Kubernetes |
| Testing | xUnit |
| Performance | Async/await patterns, parallel processing |

**Key Libraries:**

- Accord.Statistics: Hidden Markov Models, statistical analysis
- Accord.MachineLearning: Neural networks, SVMs, decision trees, random forests
- Accord.Core: Foundation for ML algorithms
- log4net: Logging

#### Key Functions/Modules for Integration

**Critical Modules:**

1. **Jube.Engine.Exhaustive.Training** - Automated model topology optimization
2. **Jube.Engine.Exhaustive.Algorithms.Unsupervised** - Anomaly detection implementation
3. **Jube.Data** - Transaction and account data management
4. **Jube.Parser** - Rule parsing and compilation
5. **Jube.Service** - Real-time processing service
6. **Jube.Cache** - Redis-based caching layer
7. **Jube.Preservation** - Configuration backup/restore
8. **Jube.Dictionary** - Data dictionary and metadata management
9. **Accord.MachineLearning.DecisionTrees** - Interpretable decision models
10. **Accord.MachineLearning.VectorMachines** - SVM-based classification

**Integration Points:**

- HTTP REST API for transaction submission
- AMQP for event streaming
- PostgreSQL for audit trail storage
- Redis for real-time state
- Webhook support for case escalations

---

### 2. AMLSim - Anti-Money Laundering Simulator

**Repository:** <https://github.com/IBM/AMLSim>

#### Main Purpose and Focus

- **Primary Goal:** Multi-agent simulator generating synthetic AML transaction data with known money laundering patterns
- **Target Users:** ML researchers, algorithm developers, AML system testers
- **Key Value:** Provides labeled synthetic data for training and validating detection algorithms
- **Problem Solved:** Addresses lack of public AML datasets (real data is sensitive/proprietary)

#### Key Features and Capabilities

**Multi-Agent Simulation Engine:**

- Agent-based modeling of bank accounts and behavior
- Statistical behavior distributions for account agents
- Realistic transaction graph generation
- Support for up to thousands of accounts
- Configurable simulation duration (steps/days)
- Reproducible simulations (seed-based)

**AML Typology Pattern Generation:**

- 8+ money laundering patterns: fan-in, fan-out, cycle, bipartite, stack, random, scatter-gather, gather-scatter
- Configurable parameters per pattern (amounts, frequencies, periods)
- Multiple pattern instances in single simulation
- Suspicious Activity Report (SAR) marking
- Alert account tracking

**Transaction Graph Generation:**

- Scale-free network generation (Watts-Strogatz, preferential attachment)
- Directed configuration model for degree distribution
- Account grouping by banks
- Edge probability weighting
- Transaction type classification
- Time-stamped transaction logs

**Normal Model Integration:**

- 6 transaction model types: single, fan_out, fan_in, mutual, forward, periodical
- Allows normal behavior interleaved with suspicious patterns
- Realistic baseline transaction generation

**Data Output:**

- CSV-based outputs
- Account lists with attributes (balance, country, business type)
- Transaction logs with timestamps and amounts
- Alert member lists (accounts participating in patterns)
- Suspicious transaction subgraphs
- Statistical analysis outputs

#### Data Models and Schemas

**Account Entity:**

```json
{
  "account_id": "string",
  "bank_id": "string",
  "initial_balance": "float",
  "country": "string",
  "business_type": "string",
  "is_sar": "boolean",
  "start_step": "int",
  "end_step": "int",
  "degree_in": "int",
  "degree_out": "int"
}
```

**Transaction Entity:**

```json
{
  "step": "int",
  "transaction_type": "string",
  "amount": "float",
  "originator_id": "string",
  "beneficiary_id": "string",
  "originator_country": "string",
  "beneficiary_country": "string",
  "is_sar": "boolean",
  "alert_id": "int",
  "originator_balance_before/after": "float",
  "beneficiary_balance_before/after": "float"
}
```

**Alert Pattern:**

```json
{
  "alert_id": "int",
  "pattern_type": "string", // fan_in, fan_out, cycle, etc.
  "account_members": ["account_id"],
  "schedule_id": "int",
  "is_sar": "boolean",
  "min_amount": "float",
  "max_amount": "float",
  "min_members": "int",
  "max_members": "int",
  "min_period": "int",
  "max_period": "int"
}
```

**Degree Distribution:**
CSV-based specification of in-degree and out-degree distributions

#### Detection/Monitoring Algorithms

**Graph Analysis Algorithms:**

1. **Diameter Computation** - Network graph diameter using HyperBall algorithm
2. **Degree Distribution Analysis** - In-degree and out-degree patterns
3. **Connected Components** - Identifying network clusters
4. **Weak Connection Count (WCC) Distribution** - Network fragmentation analysis
5. **Motif Detection** - Pattern matching in subgraphs

**Transaction Pattern Models:**

- Fan-in: Multiple sources to single sink
- Fan-out: Single source to multiple sinks
- Cycle: Circular transaction flow
- Bipartite: Two layers of accounts with transactions between
- Stack: Multiple layers of bipartite structures
- Scatter-Gather: Complex multi-stage pattern

**Feature Engineering for ML:**

- Transaction volume per account/period
- Aggregated amounts per period
- Transaction frequency
- Amount distribution metrics
- Counterparty diversity
- Temporal pattern analysis

#### Technology Stack

| Component | Technology |
|-----------|-----------|
| Core Engine | Java 8+ |
| Simulation Framework | MASON (Multi-Agent Simulator on Network) |
| Graph Analysis | WebGraph, Commons Math |
| Data Generation | Python 3.7+ |
| Graph Visualization | NetworkX, Graphviz, Matplotlib |
| Data Processing | NumPy, Pandas |
| Build System | Maven (optional), Shell scripts |
| Dependencies | JSON, SLF4J, MySQL Connector |
| Analysis | Python validation scripts |

**Key Libraries:**

- MASON v20: Multi-agent simulation framework
- WebGraph v3.6.1: Large-scale graph compression
- Commons-Math v3.6.1: Statistical/mathematical computations
- NetworkX 1.11: Graph algorithms and analysis
- Matplotlib 2.2.3: Visualization
- Powerlaw: Power-law distribution analysis

#### Key Functions/Modules for Integration

**Simulation Engine:**

1. **AMLSim.java** - Main simulator orchestrator
2. **TransactionRepository.java** - Transaction buffer and logging
3. **Account.java** - Account entity with balance management
4. **Branch.java** - Bank branch grouping
5. **AccountGroup.java** - Account grouping for pattern generation
6. **ModelParameters.java** - Transaction parameter adjustment

**Transaction Generation:**

1. **AbstractTransactionModel.java** - Base transaction model
2. **TransactionGraphGenerator.py** - Python-based transaction graph generation
3. **NormalModel.java** - Normal transaction behavior generation
4. **Alert Generation** - SAR/alert account marking

**Analysis & Validation:**

1. **Diameter.java** - Network diameter computation
2. **plot_distributions.py** - Statistical visualization
3. **network_analytics.py** - Graph algorithm analysis
4. **validate_alerts.py** - Alert pattern validation

**Configuration:**

- conf.json: Master configuration file
- paramFiles/: Account, transaction type, alert pattern specifications
- schema.json: Output CSV schema definition

---

### 3. AML-Data - Synthetic Transaction Dataset

**Repository:** <https://github.com/IBM/AML-Data>

#### Main Purpose and Focus

- **Primary Goal:** Provide open-source synthetic transaction dataset for AML research
- **Target Users:** Researchers, ML practitioners, AML system developers
- **Key Innovation:** Virtual world model-based data generation (not simple obfuscation)
- **Data Availability:** Kaggle and IBM Box repository

#### Key Features and Capabilities

**Synthetic Data Generation:**

- Virtual world simulation with banks, individuals, companies
- Statistical behavior distributions for agents
- Money laundering scenarios (smuggling, extortion, illegal gambling)
- Laundering transaction generation with labels
- ~6 billion+ in transaction volumes
- Time-series transaction data

**Transaction Scenarios:**

- Bank transfers
- Purchases
- Credit card transactions
- Checks
- Legitimate business transactions
- Money laundering transactions (labeled)

**Data Characteristics:**

- Highly realistic patterns
- Known ground truth (laundering tags)
- Temporal sequence preservation
- Network effect modeling
- Statistical validity for training ML models

#### Data Models and Schemas

**Transaction Record:**

```
txn_id, timestamp, amount, originator_id, beneficiary_id, 
originator_type, beneficiary_type, transaction_type, 
is_laundering_flag, laundering_scenario
```

**Account Record:**

```
account_id, bank_id, entity_type, entity_name, balance,
country_code, business_sector, risk_profile, created_date
```

**Entity Record:**

```
entity_id, entity_type, entity_name, address, country,
business_sector, risk_classification
```

#### Related Work

- **AMLSim (Java/Python):** More focused on simulation; this focuses on labeled dataset
- **TabFormer:** Synthetic credit card fraud data with transformer-based detection

#### Technology Stack

| Component | Technology |
|-----------|-----------|
| Format | CSV (parseable with any language) |
| Distribution | Kaggle datasets, IBM Box |
| Licensing | CDLA-Sharing-1.0 |
| Size | Multiple gigabytes |

#### Key Functions/Modules for Integration

**Data Acquisition:**

1. Download from Kaggle: AML transaction dataset
2. Download from IBM Box: Enhanced documentation
3. Schema validation: CSV field mapping

**Data Processing:**

1. Transaction parsing and validation
2. Entity resolution from transaction records
3. Time-series feature engineering
4. Pattern extraction

---

### 4. AnChainAI aml-mcp - Blockchain AML Screening

**Repository:** <https://github.com/AnChainAI/aml-mcp>

#### Main Purpose and Focus

- **Primary Goal:** Model Context Protocol (MCP) server for cryptocurrency address screening and sanctions checking
- **Target Users:** LLM/AI agents, compliance systems, crypto platforms
- **Key Innovation:** Integration with Claude/LLMs for automated AML screening via MCP
- **Unique Feature:** Multi-blockchain support (14+ protocols)

#### Key Features and Capabilities

**Cryptocurrency Address Screening:**

- Risk factor assessment for crypto addresses
- Sanctions compliance checking across blockchains
- Support for 14+ blockchains: Bitcoin, Ethereum, Solana, Stellar, Tron, Elrond, Ripple, Bitcoin Cash, Litecoin, Algorand, Bitcoin SV, Dash, Verge Currency, Zcash
- Blockchain protocol detection
- Historical transaction analysis

**Sanctions List Screening:**

- Global sanctions list integration
- Entity types: persons, companies, vessels, aircraft, crypto entities
- Search parameters: name, ID number, nationality, birth year
- Scope options: basic/full (enterprise plan)
- Multiple sanctions list sources
- Match confidence scoring

**IP Address Risk Assessment:**

- Geolocation-based country origin detection
- Sanctioned country identification
- IP reputation checking

**Model Context Protocol Integration:**

- MCP server for LLM/AI agent integration
- Designed for Claude Desktop and other MCP clients
- Tool-based architecture for easy agent invocation

#### Data Models and Schemas

**Crypto Address Screening Request:**

```python
{
  "address": "0xf4548503dd51de15e8d0e6fb559f6062d38667e7",
  "proto": "eth"  # 3-letter blockchain code
}
```

**Sanctions Screening Request:**

```python
{
  "schema": "person",  # person, company, vessel, aircraft, crypto
  "name": ["John Doe", "Jane Smith"],
  "idNumber": ["passport123"],
  "nationality": ["us", "ca"],
  "birthYear": ["1980"],
  "scope": "basic"  # basic or full
}
```

**IP Screening Request:**

```python
{
  "ip_address": "37.19.90.65"  # IPv4 or IPv6
}
```

**Response Structure:**

```python
{
  "address": "string",
  "blockchain": "string",
  "risk_score": "float",
  "sanctions_matches": [
    {
      "entity_name": "string",
      "entity_type": "string",
      "list_source": "string",
      "match_confidence": "float"
    }
  ],
  "compliance_flags": ["string"],
  "country_code": "string",
  "country_sanctions_status": "boolean"
}
```

#### Supported Blockchains

| Blockchain | Code | Coverage |
|-----------|------|----------|
| Bitcoin | btc | Full |
| Ethereum | eth | Full |
| Solana | sol | Full |
| Stellar | xlm | Full |
| Tron | trx | Full |
| Elrond | egld | Full |
| Ripple | xrp | Full |
| Bitcoin Cash | bch | Full |
| Litecoin | ltc | Full |
| Algorand | algo | Full |
| Bitcoin SV | bsv | Full |
| Dash | dash | Full |
| Verge Currency | xvg | Full |
| Zcash | zec | Full |

#### Technology Stack

| Component | Technology |
|-----------|-----------|
| Runtime | Python 3.12+ |
| Package Manager | uv |
| API Client | HTTP REST to Anchain.ai API |
| Integration | Model Context Protocol (MCP) |
| Deployment | Docker, Claude Desktop |
| Authentication | API Key-based |

**Dependencies:**

- Python 3.12+
- uv (package management)
- MCP SDK
- HTTP client libraries
- JSON serialization

#### Key Functions/Modules for Integration

**Core API Functions:**

1. **crypto_screening(address, proto)** - Screen crypto address for risk
2. **sanctions_screening(schema, name, idNumber, nationality, birthYear, scope)** - Check sanctions lists
3. **ip_screening(ip_address)** - Check IP geolocation and sanctions

**MCP Server Functions:**

1. **list_resources()** - List available tools
2. **list_tools()** - List MCP tools for agent use
3. **call_tool(name, arguments)** - Execute tool via MCP

**Configuration:**

```json
{
  "mcpServers": {
    "anchain_aml_mcp": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/aml-mcp", "--", "mcp_server.py", "--ANCHAIN_APIKEY", "api_key"]
    }
  }
}
```

**Rate Limits & Pricing:**

- See <https://aml.anchainai.com/pricing>
- Enterprise plan required for "full" scope sanctions screening

---

### 5. Anti-Money-Laundering-Project - Academic Analysis

**Repository:** <https://github.com/Janetle-hi/Anti-Money-Laundering-Project>

#### Main Purpose and Focus

- **Primary Goal:** Analyze real-world AML case using public transaction data
- **Target Users:** Data analysts, researchers, students
- **Key Value:** Demonstrates transaction pattern analysis on real Danske Bank scandal data
- **Data Source:** Organized Crime and Corruption Reporting Project (OCCRP)

#### Key Features and Capabilities

**Case Study: Azerbaijani Laundromat**

- Transaction period: June 2012 - End 2014
- Total transactions: 16,821 payments
- Total amount: $6+ billion
- Key finding: UK-registered firms moving $2.9 billion
- Suspicious parties: Polux Management LP, Hilux Services LP, Metastar Invest LLP, LCM Alliance LLP

**Analysis Techniques:**

- Time-series transaction analysis
- Entity relationship mapping
- Aggregated amount analysis
- Transaction flow visualization
- Network relationship discovery
- Pattern identification (concentration, velocity)

**Key Findings:**

- 70%+ of transactions from 4 suspicious companies
- Unusual activity indicators
- Money flows to beneficiaries including high officials' family members
- Some transactions with unclear descriptions/recipients
- Suspected use for economic and political purposes

#### Data Models and Schemas

**Transaction Record (JSON-based):**

```json
{
  "transaction_date": "YYYY-MM-DD",
  "originator_name": "string",
  "originator_account": "string",
  "beneficiary_name": "string",
  "beneficiary_account": "string",
  "amount": "float",
  "currency": "string",
  "transaction_description": "string"
}
```

#### Technology Stack

| Component | Technology |
|-----------|-----------|
| Analysis | Python |
| Visualization | Tableau |
| Notebooks | Jupyter |
| Data Format | JSON |
| Libraries | Pandas, NumPy, Matplotlib |

#### Key Functions/Modules for Integration

**Analysis Modules:**

1. **Transaction aggregation** - Sum amounts by entity, time period
2. **Entity relationship mapping** - Build transaction networks
3. **Pattern detection** - Identify concentration and velocity anomalies
4. **Visualization** - Network diagrams, time-series charts

**Integration Points:**

- Export transaction data to CSV for analysis
- Build entity graphs from transaction relationships
- Apply time-windowed aggregation functions
- Detect anomalous patterns

---

### 6. Databricks Industry Solutions - AML Analytics

**Repository:** <https://github.com/databricks-industry-solutions/anti-money-laundering>

#### Main Purpose and Focus

- **Primary Goal:** Enterprise-scale AML solution on Lakehouse platform combining graph analytics, NLP, and computer vision
- **Target Users:** Enterprise data teams, compliance departments, data engineers
- **Key Innovation:** Lakehouse approach (Delta Lake) + GraphFrames for advanced AML patterns
- **Architecture:** Multi-notebook pipeline orchestration

#### Key Features and Capabilities

**1. Network Analysis & Graph Patterns:**

- Connected component analysis for entity networks
- Synthetic identity detection (multiple IDs, shared attributes)
- Motif finding for complex transaction patterns
- Structured graph search patterns

**Patterns Detected:**

- **Structuring/Smurfing:** Multiple entities → aggregate payments → final bank
  - Pattern: Multiple small payments under threshold aggregating to large amount
  - Detection: Graph motifs finding pattern structures
  
- **Round-Tripping:** Circular fund flow (A → B → C → D → A)
  - Detection: Graph cycle detection
  - Visualization: Motif patterns with entity names
  
- **Synthetic Identities:** Multiple accounts sharing attributes (address, phone, email)
  - Detection: Connected components on attribute graph
  - Risk Scoring: Shared attribute count → synthetic score

- **Risk Propagation:** Influence spread through transaction network
  - Detection: Pregel API for iterative message passing
  - Algorithm: Risk score propagation through 3+ layers
  - Use case: Politically exposed persons (PEP) influencing connected entities

**2. Address Verification & Computer Vision:**

- Google Street View API integration for address validation
- Pre-trained VGG16 model for property classification
- Image-based address legitimacy assessment
- Support for 100+ concurrent image fetches

**3. Entity Resolution/Deduplication:**

- Splink library for probabilistic entity matching
- Fuzzy matching on organization names, addresses
- Blocking rules for computational efficiency
- Match probability scoring (Expectation-Maximization framework)
- Multi-field deduplication

**4. Data Pipeline Orchestration:**

- 4-notebook orchestrated pipeline
- Sequential task dependencies
- MLflow experiment tracking
- Delta Lake time-travel and versioning

#### Data Models and Schemas

**Transaction Entity:**

```sql
CREATE TABLE transactions (
  txn_id STRING,
  originator_id STRING,
  beneficiary_id STRING,
  txn_amount DOUBLE,
  txn_date TIMESTAMP,
  originator_country STRING,
  beneficiary_country STRING,
  rptd_originator_name STRING,
  rptd_beneficiary_name STRING,
  rptd_originator_address STRING,
  rptd_beneficiary_address STRING
)
```

**Entity Record:**

```sql
CREATE TABLE entities (
  entity_id STRING,
  entity_type STRING,  -- Person, Company, etc.
  name STRING,
  address STRING,
  country STRING,
  email_addr STRING,
  phone_number STRING,
  risk_score DOUBLE,
  entity_classification STRING
)
```

**Connected Components (Synthetic IDs):**

```sql
CREATE TABLE ptntl_synthetic_ids (
  id STRING,
  component BIGINT,
  type STRING,  -- Person, Address, Email, Phone
  shared_attribute_count INT,
  synth_score INT
)
```

**Structuring Pattern Detection:**

```sql
CREATE TABLE structuring_patterns (
  pattern_id STRING,
  layer_0_entity STRING,  -- Initial source
  layer_1_entity STRING,  -- Intermediate
  layer_2_entity STRING,  -- Aggregation point
  layer_3_entity STRING,  -- Final destination (often company)
  total_amount DOUBLE,
  pattern_type STRING
)
```

**Round-Trip Motifs:**

```sql
CREATE TABLE roundtrips (
  path_a STRING,  -- Source entity
  path_b STRING,  -- Intermediate
  path_c STRING,  -- Intermediate
  path_d STRING,  -- Final (returns to A)
  total_amount DOUBLE,
  num_hops INT
)
```

**Risk Propagation Graph:**

```sql
CREATE TABLE risk_propagation (
  id STRING,
  risk_score DOUBLE,
  original_risk DOUBLE,
  risk_origin_distance INT,
  entity_name STRING
)
```

**Entity Deduplication Scores:**

```sql
CREATE TABLE dedupe_records (
  org_name_l STRING,
  org_name_r STRING,
  org_name_match_score DOUBLE,
  address_l STRING,
  address_r STRING,
  address_match_score DOUBLE,
  amount_l DOUBLE,
  amount_r DOUBLE,
  amount_match_score DOUBLE,
  final_match_probability DOUBLE
)
```

#### Detection/Monitoring Algorithms

**1. Connected Components Algorithm:**

- Input: Graph of entities connected by shared attributes
- Process: Iterative traversal of all reachable nodes
- Output: Component assignment to each entity
- Use: Identify entity groups that should be same person (synthetic IDs)

**2. Motif Finding (Pattern Matching):**

- Query language: Graph motif patterns with multi-vertex edges
- Pattern: "(a)-[e1]->(b); (b)-[e2]->(c); ..."
- Matching: Find all subgraphs matching pattern
- Examples:
  - Structuring: 5-entity motif with aggregation point
  - Round-trips: 4-entity cycle pattern

**3. Pregel Message Passing (Risk Propagation):**

- Algorithm: Iterative message passing on graph
- Initialization: Known risk entities have initial risk score
- Iteration: Risk score propagated to neighbors
- Aggregation: Each node updates risk based on incoming messages
- Convergence: Max iterations (typically 3)

**4. Probabilistic Entity Matching (Splink):**

- Framework: Expectation-Maximization (EM)
- Blocking: Group candidates by key fields (amount, date)
- Comparison: Field-by-field similarity scoring
- Probability: Bayesian calculation of match probability
- Visualization: Charts showing probability distribution

#### Technology Stack

| Layer | Technology |
|-------|-----------|
| Platform | Databricks (Spark cluster) |
| Compute | Apache Spark 11.3 ML Runtime |
| Data Lake | Delta Lake |
| Language | PySpark (Python on Spark) |
| Graph Processing | GraphFrames |
| Entity Matching | Splink 2.1.14 |
| Computer Vision | PyTorch, VGG16, Pillow |
| APIs | Google Street View API |
| Orchestration | Databricks Workflow |
| ML Tracking | MLflow |
| Visualization | Databricks SQL, Plots |

**Key Libraries:**

- **graphframes:** Graph analytics (connected components, motif finding, PageRank)
- **splink:** Probabilistic record linkage
- **torch:** Deep learning for image processing
- **torchvision:** Pre-trained computer vision models
- **Pillow (PIL):** Image processing

#### Key Functions/Modules for Integration

**Graph Analysis Functions:**

1. **Connected Components:**

```python
result = graph.connectedComponents()
result.select("id", "component", "type")
```

1. **Motif Finding:**

```python
motif = "(a)-[e1]->(b); (b)-[e2]->(c); (d)-[e3]->(f); (f)-[e5]->(c); (c)-[e6]->(g)"
patterns = graph.find(motif)
```

1. **Pregel API (Message Passing):**

```python
ranks = graph.pregel \
  .setMaxIter(3) \
  .withVertexColumn("risk_score", col("risk"), ...) \
  .sendMsgToDst(Pregel.src("risk_score")/2) \
  .aggMsgs(sum(Pregel.msg())) \
  .run()
```

**Entity Resolution Functions:**

1. **Splink Matching:**

```python
from splink import Splink
settings = { "link_type": "dedupe_only", "blocking_rules": [...] }
linker = Splink(settings, df, spark)
scored = linker.get_scored_comparisons()
```

1. **Match Probability Visualization:**

```python
model = linker.model
model.probability_distribution_chart()
model.all_charts_write_html_file("output.html")
```

**Computer Vision Functions:**

1. **Pre-trained Model Prediction:**

```python
vgg = models.vgg16(pretrained=True)
prediction = vgg(img)
predicted_class = prediction.data.numpy().argmax()
```

1. **Image Processing Pipeline:**

```python
transform = transforms.Compose([
  transforms.Resize(224),
  transforms.ToTensor(),
  transforms.Normalize(mean=[0.485, 0.456, 0.406],
                      std=[0.229, 0.224, 0.225])
])
```

**Notebooks in Pipeline:**

1. `00_aml_context.py` - Setup and context
2. `01_aml_network_analysis.py` - Graph patterns, synthetic IDs, structuring, round-trips, risk propagation
3. `02_aml_address_verification.py` - Street view API, computer vision classification
4. `03_aml_entity_resolution.py` - Splink-based entity matching and deduplication

---

## Comparative Analysis

### Feature Comparison Matrix

| Feature | Jube | AMLSim | AML-Data | aml-mcp | Academic | Databricks |
|---------|------|--------|----------|---------|----------|-----------|
| **Real-time Monitoring** | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Case Management** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Synthetic Data Gen** | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ |
| **ML Models** | ✓ | ✗ | Implicit | ✗ | Implicit | ✓ |
| **Rule Engine** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Sanctions Screening** | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Crypto Support** | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Graph Analytics** | ✗ | ✓ | Implicit | ✗ | ✓ | ✓ |
| **Computer Vision** | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Entity Resolution** | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Multi-tenant** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Cloud-Native** | ✓ | Partial | ✗ | ✓ | ✗ | ✓ |
| **Open Source** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Production Ready** | ✓ | ✓ | ✓ | Emerging | Academic | ✓ |

### Architecture Patterns

**Transaction Processing:**

- **Jube:** Real-time streaming (Redis-based)
- **AMLSim:** Batch simulation
- **Databricks:** Batch/streaming via Spark

**Detection Approach:**

- **Jube:** Hybrid (ML + rules)
- **AMLSim:** Simulation-based ground truth
- **Databricks:** Graph motifs + ML
- **aml-mcp:** API-based lookups

**Data Flow:**

- **Jube:** HTTP/AMQP → Redis → PostgreSQL
- **AMLSim:** Configuration → Java Engine → CSV
- **Databricks:** Delta Lake → GraphFrames → SQL

### Scalability Characteristics

| Aspect | Jube | AMLSim | Databricks |
|--------|------|--------|-----------|
| **Accounts** | Millions (horizontal scale) | Thousands (simulation scale) | Billions (Spark scale) |
| **Transactions/sec** | High (real-time) | Moderate (simulation) | Very high (batch) |
| **Network Size** | Large-scale graphs | Medium (agent-based) | Enterprise (distributed) |
| **Deployment** | Docker/K8s | Single machine/cluster | Databricks cluster |
| **Multi-tenancy** | Yes | No | Limited |

---

## Integration Recommendations

### For Your Existing AML System

#### 1. **Primary Integration: Jube Engine**

**Rationale:**

- Mature, production-ready real-time monitoring
- Complements existing system (case management, rules)
- Open-source (AGPLv3) - no licensing conflicts
- .NET native (compatible with your codebase)

**Integration Points:**

```
Your System ↔ Jube Rules Engine ↔ Transaction Detection
     ↓
Your Case Mgmt ↔ Jube Case Workflows (optional)
     ↓
Your DB ↔ PostgreSQL (Jube audit logs)
```

**Recommended Modules to Adopt:**

1. `Jube.Engine.Exhaustive` - ML-based risk scoring
2. `Accord.MachineLearning.*` - Decision trees, random forests for interpretable alerts
3. `Jube.Parser` - Rule compilation and execution
4. `Jube.Cache` - Redis-based velocity counters

**API Integration:**

```csharp
// Submit transaction
POST /api/transactions/{entityId}/{caseId}
{
  "amount": 5000,
  "counterparty": "ACME Corp",
  "timestamp": "2026-02-01T10:00:00Z"
}

// Get risk score
GET /api/risks/{entityId}
→ { "risk_score": 0.78, "factors": [...] }
```

#### 2. **Secondary Integration: AMLSim for Testing**

**Rationale:**

- Generate labeled test data for your ML models
- Validate detection algorithms before production
- Benchmark rule engine performance

**Integration Flow:**

```
1. Configure AMLSim with your AML patterns of interest
2. Generate synthetic transaction dataset (CSV)
3. Load into test database
4. Run detection engine
5. Validate detection rates against known patterns
```

**Configuration Template:**

```json
{
  "general": {
    "simulation_name": "your_test_scenario",
    "total_steps": 365,
    "base_date": "2025-01-01"
  },
  "input": {
    "directory": "paramFiles/",
    "accounts": "accounts.csv",
    "alert_patterns": "alertPatterns.csv"
  },
  "output": {
    "directory": "outputs/",
    "transactions": "transactions.csv",
    "alert_members": "alert_accounts.csv"
  }
}
```

#### 3. **Tertiary Integration: Databricks for Analytics**

**Rationale:**

- Scalable graph analysis on large transaction volumes
- Computer vision for address verification (KYC enhancement)
- Entity resolution for deduplication

**Use Cases for Your System:**

1. **Batch Synthetic ID Detection:**
   - Daily batch processing of all transactions
   - Connected component analysis for shared attributes
   - Risk scoring for synthetic identity rings

2. **Pattern Discovery:**
   - Find previously unknown structuring patterns
   - Detect round-trip laundering schemes
   - Identify high-risk entity clusters

3. **Address Verification:**
   - Validate client-provided addresses against Street View
   - Flag suspicious/non-existent properties
   - Support enhanced KYC process

**Databricks Notebook Structure for Your System:**

```python
# 1. Load your transaction data from your DB
transactions = spark.read.jdbc(your_db_config)

# 2. Build entity graph
nodes = transactions.select("originator_id").union(...)
edges = transactions.select("originator_id", "beneficiary_id", "amount", ...)
g = GraphFrame(nodes, edges)

# 3. Run connected components for synthetic IDs
components = g.connectedComponents()

# 4. Save results back to your database
components.write.jdbc(your_db_config, mode="overwrite")
```

#### 4. **Crypto AML: AnChainAI Integration**

**Rationale:**

- If your system processes crypto transactions
- Screen addresses for sanctions/risk flags
- Add crypto compliance layer

**Integration:**

```python
# In your transaction validation
from aml_mcp import crypto_screening, sanctions_screening

if transaction.currency == "crypto":
    risk_result = crypto_screening(transaction.wallet_address, "eth")
    if risk_result["sanctions_matches"]:
        flag_for_review(transaction)
```

---

## Technical Implementation Guide

### Phase 1: Foundation (Weeks 1-4)

#### 1.1 Implement Jube ML Models

**Objective:** Add adaptive ML-based risk scoring to your system

**Tasks:**

1. Integrate Accord.NET libraries:

   ```xml
   <PackageReference Include="Accord" Version="3.8.0" />
   <PackageReference Include="Accord.MachineLearning" Version="3.8.0" />
   <PackageReference Include="Accord.Statistics" Version="3.8.0" />
   ```

2. Implement `BehavioralAnalyzer` module:

   ```csharp
   public class BehavioralAnalyzer
   {
       private double[][] _trainingFeatures;
       private int[] _trainingLabels;
       private DecisionTree _model;
       
       public void Train(List<Transaction> transactions)
       {
           _trainingFeatures = ExtractFeatures(transactions);
           _trainingLabels = transactions.Select(t => t.IsAML ? 1 : 0).ToArray();
           
           var teacher = new C45Learning();
           _model = teacher.Learn(_trainingFeatures, _trainingLabels);
       }
       
       public double GetRiskScore(Transaction transaction)
       {
           var features = ExtractFeatures(new[] { transaction });
           return _model.Decide(features[0]);
       }
       
       private double[][] ExtractFeatures(List<Transaction> transactions)
       {
           // Transaction amount, frequency, velocity, counterparty risk, etc.
           return transactions.Select(t => new[]
           {
               (double)t.Amount,
               GetVelocity(t),
               GetCounterpartyRisk(t.CounterpartyId),
               GetGeographicRisk(t.BeneficiaryCountry)
           }).ToArray();
       }
   }
   ```

3. Create `VelocityCounter` (Redis-backed):

   ```csharp
   public class VelocityCounter
   {
       private IDatabase _redis;
       
       public void RecordTransaction(string accountId, decimal amount, int timeWindowMinutes)
       {
           var key = $"velocity:{accountId}:{DateTime.Now.AddMinutes(-timeWindowMinutes)}";
           _redis.ListLeftPush(key, amount.ToString());
           _redis.KeyExpire(key, TimeSpan.FromMinutes(timeWindowMinutes * 2));
       }
       
       public decimal GetVelocity(string accountId, int timeWindowMinutes)
       {
           var key = $"velocity:{accountId}:*";
           var values = _redis.ListRange(key, 0, -1);
           return values.Sum(v => decimal.Parse(v.ToString()));
       }
   }
   ```

#### 1.2 Set Up AMLSim Test Data Generation

**Objective:** Create realistic test dataset for validation

**Tasks:**

1. Clone AMLSim repository
2. Configure paramFiles:

   ```csv
   # alertPatterns.csv
   count,type,schedule_id,min_accounts,max_accounts,min_amount,max_amount,min_period,max_period,bank_id,is_sar
   10,fan_in,1,3,5,1000,5000,30,90,BANK1,1
   5,fan_out,1,3,5,2000,8000,30,60,BANK2,1
   ```

3. Generate synthetic transactions:

   ```bash
   cd AMLSim
   python3 scripts/transaction_graph_generator.py conf.json
   sh scripts/build_AMLSim.sh
   sh scripts/run_AMLSim.sh conf.json
   ```

4. Load CSV outputs into test database
5. Validate detection rates

### Phase 2: Advanced Analytics (Weeks 5-8)

#### 2.1 Graph Analysis for Pattern Detection

**Objective:** Detect complex laundering patterns (structuring, round-trips)

**Tasks:**

1. Set up Databricks environment
2. Implement pattern detection notebook:

   ```python
   # In Databricks notebook
   from graphframes import GraphFrame
   
   # Build graph
   edges = spark.read.table("transactions")
   nodes = edges.select("originator_id").union(edges.select("beneficiary_id"))
   graph = GraphFrame(nodes, edges)
   
   # Detect structuring pattern
   motif = "(a)-[e1]->(b); (b)-[e2]->(c); (c)-[e3]->(d); (d)-[e4]->(a)"
   cycles = graph.find(motif)
   ```

3. Create `PatternDetector` service:

   ```csharp
   public class PatternDetector
   {
       public async Task<List<SuspiciousPattern>> DetectPatternsAsync(
           DateTime startDate, DateTime endDate)
       {
           var patterns = new List<SuspiciousPattern>();
           
           // Query Databricks results
           var structuring = await _databricksClient.QueryAsync(
               "SELECT * FROM structuring_patterns WHERE pattern_date BETWEEN ? AND ?",
               startDate, endDate);
           
           foreach (var pattern in structuring)
           {
               patterns.Add(new SuspiciousPattern
               {
                   Type = PatternType.Structuring,
                   Entities = pattern.Entities,
                   TotalAmount = pattern.Amount,
                   Severity = CalculateSeverity(pattern)
               });
           }
           
           return patterns;
       }
   }
   ```

#### 2.2 Entity Resolution Integration

**Objective:** Detect duplicate/synthetic identities

**Tasks:**

1. Implement entity matching workflow:

   ```python
   # Python script to run in Databricks
   from splink import Splink
   
   settings = {
       "link_type": "dedupe_only",
       "blocking_rules": ["l.country = r.country"],
       "comparison_columns": [
           {"col_name": "entity_name", "term_frequency_adjustments": True},
           {"col_name": "address"},
           {"col_name": "phone_number"}
       ]
   }
   
   df = spark.read.table("entities")
   linker = Splink(settings, df, spark)
   matches = linker.get_scored_comparisons()
   
   # Flag high-confidence matches as synthetic IDs
   suspicious = matches.filter(col("match_probability") > 0.95)
   suspicious.write.mode("overwrite").saveAsTable("synthetic_id_candidates")
   ```

2. Create alert workflow for matches:

   ```csharp
   public class EntityResolutionAlerter
   {
       public async Task ProcessSyntheticIDCandidatesAsync()
       {
           var candidates = await _databricksClient.GetSyntheticIDCandidatesAsync();
           
           foreach (var candidate in candidates)
           {
               var alert = new Alert
               {
                   AlertType = AlertType.SyntheticIdentity,
                   Entities = candidate.MatchingEntities,
                   MatchConfidence = candidate.MatchProbability,
                   Severity = AlertSeverity.High,
                   RecommendedAction = "Manual Review Required"
               };
               
               await _caseManager.CreateCaseAsync(alert);
           }
       }
   }
   ```

### Phase 3: Real-Time Enhancement (Weeks 9-12)

#### 3.1 Real-Time Velocity Checks

**Objective:** Detect rapid transaction patterns

**Implementation:**

```csharp
public class RealTimeVelocityEngine
{
    private readonly IConnectionMultiplexer _redis;
    private readonly ITransactionRepository _db;
    
    public async Task<RiskAssessment> AssessTransactionAsync(Transaction txn)
    {
        var assessment = new RiskAssessment();
        
        // Check 1-hour velocity
        var hourlyVolume = await GetVelocityAsync(
            txn.AccountId, AccountId, TimeSpan.FromHours(1));
        if (hourlyVolume > 100000)
            assessment.AddFlag(RiskFactor.HighVelocity, 0.8);
        
        // Check daily velocity
        var dailyVolume = await GetVelocityAsync(
            txn.AccountId, TimeSpan.FromDays(1));
        if (dailyVolume > 500000)
            assessment.AddFlag(RiskFactor.ExtremeVelocity, 0.95);
        
        // Check counterparty risk
        var counterpartyRisk = await _db.GetCounterpartyRiskAsync(
            txn.BeneficiaryId);
        if (counterpartyRisk > 0.7)
            assessment.AddFlag(RiskFactor.HighRiskCounterparty, counterpartyRisk);
        
        // Calculate final score
        assessment.FinalScore = CalculateCombinedScore(assessment.Flags);
        
        if (assessment.FinalScore > 0.85)
            await _alertManager.CreateAlertAsync(txn, assessment);
        
        return assessment;
    }
    
    private async Task<decimal> GetVelocityAsync(
        string accountId, TimeSpan window)
    {
        var db = _redis.GetDatabase();
        var key = $"velocity:{accountId}";
        var cutoff = DateTime.UtcNow.Subtract(window);
        
        var transactions = await _db.GetTransactionsAsync(
            accountId, cutoff, DateTime.UtcNow);
        
        return transactions.Sum(t => t.Amount);
    }
}
```

#### 3.2 Sanctions List Integration

**Objective:** Real-time sanctions screening

**Implementation:**

```csharp
public class SanctionsScreeningEngine
{
    private readonly HttpClient _anchainClient;
    private readonly ICache _sanctionsCache;
    
    public async Task<SanctionsMatch> ScreenAddressAsync(
        string cryptoAddress, string blockchain)
    {
        // Check cache first
        var cacheKey = $"crypto:{blockchain}:{cryptoAddress}";
        if (_sanctionsCache.TryGet(cacheKey, out SanctionsMatch cached))
            return cached;
        
        // Call AnChain API
        var response = await _anchainClient.PostAsJsonAsync(
            "/api/crypto/screen",
            new { address = cryptoAddress, protocol = blockchain });
        
        var result = await response.Content.ReadAsAsync<SanctionsMatch>();
        
        // Cache for 24 hours
        _sanctionsCache.Set(cacheKey, result, TimeSpan.FromHours(24));
        
        return result;
    }
    
    public async Task<SanctionsMatch> ScreenEntityAsync(
        string name, string nationality, int? birthYear)
    {
        var response = await _anchainClient.PostAsJsonAsync(
            "/api/sanctions/screen",
            new
            {
                schema = "person",
                name = new[] { name },
                nationality = new[] { nationality },
                birthYear = birthYear.HasValue ? new[] { birthYear } : null,
                scope = "basic"
            });
        
        return await response.Content.ReadAsAsync<SanctionsMatch>();
    }
}
```

#### 3.3 Automated Alert Generation

**Objective:** Create alerts from detected patterns

**Implementation:**

```csharp
public class AutomatedAlertEngine
{
    private readonly IAlertRepository _alertRepo;
    private readonly IRuleEngine _ruleEngine;
    private readonly INotificationService _notifications;
    
    public async Task ProcessDetectionsAsync(DetectionBatch batch)
    {
        var alerts = new List<Alert>();
        
        // Process ML-based detections
        foreach (var detection in batch.MLDetections)
        {
            if (detection.RiskScore > 0.75)
            {
                var alert = CreateMLBasedAlert(detection);
                alerts.Add(alert);
            }
        }
        
        // Process rule-based detections
        foreach (var violation in batch.RuleViolations)
        {
            var alert = CreateRuleBasedAlert(violation);
            alerts.Add(alert);
        }
        
        // Process graph pattern detections
        foreach (var pattern in batch.GraphPatterns)
        {
            var alert = CreatePatternAlert(pattern);
            alerts.Add(alert);
        }
        
        // Save all alerts
        await _alertRepo.SaveBatchAsync(alerts);
        
        // Notify analysts
        foreach (var alert in alerts.Where(a => a.Severity == AlertSeverity.Critical))
        {
            await _notifications.NotifyAnalystAsync(alert);
        }
    }
    
    private Alert CreateMLBasedAlert(MLDetection detection)
    {
        return new Alert
        {
            AlertId = Guid.NewGuid().ToString(),
            AlertType = AlertType.MachineLearning,
            AccountId = detection.AccountId,
            RiskScore = detection.RiskScore,
            RiskFactors = detection.Factors,
            SourceSystem = "Adaptive ML Engine",
            Severity = MapRiskScoreToSeverity(detection.RiskScore),
            CreatedAt = DateTime.UtcNow,
            Status = AlertStatus.New,
            InvestigationRequired = true
        };
    }
}
```

---

### Configuration Templates

#### Redis Configuration for Velocity Counters

```json
{
  "redis": {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "password": "secure_password",
    "ssl": true,
    "ttl_minutes": 1440
  },
  "velocity_thresholds": {
    "hourly_max": 100000,
    "daily_max": 500000,
    "weekly_max": 2000000
  }
}
```

#### ML Model Configuration

```json
{
  "ml_models": {
    "decision_tree": {
      "max_depth": 10,
      "min_samples_leaf": 5,
      "enabled": true
    },
    "random_forest": {
      "n_trees": 100,
      "max_depth": 15,
      "enabled": true
    },
    "svm": {
      "kernel": "rbf",
      "c_parameter": 1.0,
      "enabled": false
    }
  },
  "feature_selection": {
    "transaction_amount": 1.0,
    "velocity_score": 0.8,
    "counterparty_risk": 0.7,
    "geographic_risk": 0.6
  },
  "retraining_schedule": "weekly",
  "min_confidence_threshold": 0.75
}
```

#### Graph Analysis Configuration

```json
{
  "databricks": {
    "workspace_url": "https://your-workspace.databricks.com",
    "token": "secure_token",
    "cluster_id": "your-cluster-id"
  },
  "patterns": {
    "structuring": {
      "min_layers": 3,
      "min_amount": 50000,
      "time_window_days": 90
    },
    "round_trips": {
      "max_hops": 4,
      "min_amount": 25000
    },
    "synthetic_ids": {
      "min_matching_attributes": 2,
      "match_confidence_threshold": 0.95
    }
  }
}
```

---

## Summary: Implementation Roadmap

| Phase | Week | Component | Outcome |
|-------|------|-----------|---------|
| **1: Foundation** | 1-4 | Jube ML models, AMLSim testing | Baseline ML risk scoring + test data |
| **2: Analytics** | 5-8 | Databricks integration, entity resolution | Pattern detection + synthetic ID detection |
| **3: Real-time** | 9-12 | Velocity engine, sanctions screening, alerts | Production-ready real-time system |
| **Post-Launch** | 13+ | Continuous improvement, model retraining | Ongoing optimization |

---

## Key Success Metrics

1. **Detection Accuracy:** > 90% precision on known patterns
2. **False Positive Rate:** < 5% (to avoid analyst fatigue)
3. **Alert Response Time:** < 1 second from detection to case creation
4. **System Uptime:** > 99.9%
5. **Model Retraining Frequency:** Weekly or on-demand
6. **Coverage:** 100% of transactions within 24 hours
7. **Entity Resolution:** > 95% match accuracy for duplicates

---

## References & Additional Resources

- **Jube Documentation:** <https://jube-home.github.io/aml-fraud-transaction-monitoring/>
- **AMLSim Wiki:** <https://github.com/IBM/AMLSim/wiki/>
- **Databricks AML Blog:** <https://www.databricks.com/blog/2021/07/16/aml-solutions-at-scale-using-databricks-lakehouse-platform.html>
- **Splink Documentation:** <https://moj-analytical-services.github.io/splink/>
- **GraphFrames Guide:** <https://graphframes.github.io/graphframes/docs/_site/>
- **AnChain.AI Documentation:** <https://aml.anchainai.com/docs>

---

**End of Analysis Document**
**Generated:** February 1, 2026 | **Status:** Complete and Ready for Implementation
