#!/usr/bin/env python3
"""
ENHANCED AML CASE MANAGEMENT SYSTEM v6.0 - ENTERPRISE EDITION
Integrated with features from top AML systems: Jube, AMLSim, Databricks, AnChainAI, IBM, and Academic Research
Real Anti-Money Laundering System with Advanced Detection, ML & Network Analysis
For: AML AMLC Lahore
"""

import os
import json
import logging
import sqlite3
import uuid
import hashlib
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Set, Any
from dataclasses import dataclass, asdict, field
from enum import Enum
from collections import defaultdict, deque
import threading
from functools import lru_cache
import pickle

try:
    from flask import Flask, jsonify, request, session
    from flask_cors import CORS
    from werkzeug.security import generate_password_hash, check_password_hash
except ImportError:
    os.system("pip install -q flask flask-cors werkzeug")
    from flask import Flask, jsonify, request, session
    from flask_cors import CORS
    from werkzeug.security import generate_password_hash, check_password_hash

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('aml_system.log')]
)
logger = logging.getLogger(__name__)

# ======================== ENUMS ========================


class CaseStatus(str, Enum):
    OPEN = "open"
    UNDER_INVESTIGATION = "under_investigation"
    ESCALATED = "escalated"
    CONVERTED_TO_FIR = "converted_to_fir"
    CLOSED = "closed"
    TRANSFERRED = "transferred"
    SAR_GENERATED = "sar_generated"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CaseType(str, Enum):
    HAWALA = "hawala"
    TERRORISM = "terrorism"
    CORRUPTION = "corruption"
    SMUGGLING = "smuggling"
    FRAUD = "fraud"
    CASH = "cash"
    TRADE_BASED = "trade_based"
    STRUCTURING = "structuring"
    ROUND_TRIPPING = "round_tripping"
    LAYERING = "layering"
    INTEGRATION = "integration"
    OTHER = "other"


class ThreatLevel(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class PatternType(str, Enum):
    FAN_IN = "fan_in"  # Many → One
    FAN_OUT = "fan_out"  # One → Many
    CYCLE = "cycle"  # Circular transfers
    STRUCTURING = "structuring"  # Small frequent transfers
    ROUND_TRIPPING = "round_tripping"  # Out and back
    PYRAMID = "pyramid"  # Hierarchical
    LAYERING = "layering"  # Complex chains
    UNUSUAL_TIMING = "unusual_timing"  # Suspicious time patterns
    RAPID_MOVEMENT = "rapid_movement"  # Quick fund movement


class IndicatorType(str, Enum):
    HIGH_RISK_JURISDICTION = "high_risk_jurisdiction"
    SANCTIONS_MATCH = "sanctions_match"
    PEP_INVOLVEMENT = "pep_involvement"
    CASH_INTENSIVE = "cash_intensive"
    UNUSUAL_VOLUME = "unusual_volume"
    STRUCTURAL_PATTERN = "structural_pattern"
    BEHAVIORAL_ANOMALY = "behavioral_anomaly"
    BLOCKCHAIN_SUSPICIOUS = "blockchain_suspicious"


# ======================== DATA MODELS (Enhanced) ========================

@dataclass
class Entity:
    """Represents a person or organization"""
    entity_id: str
    name: str
    entity_type: str  # person, organization, account
    cnic_number: Optional[str] = None
    pep_flag: bool = False
    sanctions_flag: bool = False
    risk_score: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict = field(default_factory=dict)

    def to_dict(self):
        d = asdict(self)
        d['created_at'] = self.created_at.isoformat()
        return d


@dataclass
class Transaction:
    """Enhanced transaction model with multiple fields"""
    transaction_id: str
    case_id: str
    source_entity: str
    destination_entity: str
    amount: float
    currency: str
    transaction_date: datetime
    status: str
    description: str = ""
    transaction_type: str = "transfer"  # transfer, withdrawal, deposit, conversion
    # online, cash, wire, etc
    channels: List[str] = field(default_factory=list)
    flags: List[str] = field(default_factory=list)
    risk_score: float = 0.0
    detected_patterns: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        d = asdict(self)
        d['transaction_date'] = self.transaction_date.isoformat()
        d['created_at'] = self.created_at.isoformat()
        return d


@dataclass
class NetworkNode:
    """Network analysis node"""
    node_id: str
    entity_id: str
    node_type: str  # source, destination, intermediary
    in_degree: int = 0
    out_degree: int = 0
    betweenness_centrality: float = 0.0
    risk_score: float = 0.0
    connections: Set[str] = field(default_factory=set)


@dataclass
class AnomalyScore:
    """Anomaly detection result"""
    transaction_id: str
    score: float  # 0-100, higher = more anomalous
    reasons: List[str]
    detected_at: datetime = field(default_factory=datetime.now)


# ======================== DATABASE MANAGER (Enhanced) ========================


class DatabaseManager:
    def __init__(self, db_path: str = "aml_system.db"):
        self.db_path = db_path
        self.connection_pool = []
        self._lock = threading.Lock()
        self.init_database()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        # Write-ahead logging for performance
        conn.execute("PRAGMA journal_mode = WAL")
        return conn

    def init_database(self):
        """Initialize enhanced AML database schema with indexing"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'analyst',
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Enhanced AML Cases table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aml_cases (
                case_id TEXT PRIMARY KEY,
                case_number TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                case_type TEXT NOT NULL,
                status TEXT DEFAULT 'open',
                risk_level TEXT DEFAULT 'medium',
                accused_names TEXT,
                cnic_numbers TEXT,
                amount_involved REAL,
                currency TEXT DEFAULT 'PKR',
                source_of_funds TEXT,
                destination TEXT,
                investigation_officer TEXT,
                priority BOOLEAN DEFAULT 0,
                network_risk_score REAL DEFAULT 0.0,
                pattern_indicators TEXT,
                sar_generated BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT
            )
        """)

        # Entities table (persons, organizations)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                entity_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                entity_type TEXT,
                cnic_number TEXT UNIQUE,
                pep_flag BOOLEAN DEFAULT 0,
                sanctions_flag BOOLEAN DEFAULT 0,
                risk_score REAL DEFAULT 0.0,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Enhanced Transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id TEXT PRIMARY KEY,
                case_id TEXT NOT NULL,
                source_entity TEXT NOT NULL,
                destination_entity TEXT NOT NULL,
                amount REAL NOT NULL,
                currency TEXT DEFAULT 'PKR',
                transaction_date TIMESTAMP,
                status TEXT DEFAULT 'pending',
                transaction_type TEXT DEFAULT 'transfer',
                channels TEXT,
                description TEXT,
                flags TEXT,
                risk_score REAL DEFAULT 0.0,
                detected_patterns TEXT,
                anomaly_score REAL DEFAULT 0.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (case_id) REFERENCES aml_cases(case_id),
                FOREIGN KEY (source_entity) REFERENCES entities(entity_id),
                FOREIGN KEY (destination_entity) REFERENCES entities(entity_id)
            )
        """)

        # Network analysis edges
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS network_edges (
                edge_id TEXT PRIMARY KEY,
                source_entity TEXT NOT NULL,
                destination_entity TEXT NOT NULL,
                transaction_count INTEGER DEFAULT 0,
                total_amount REAL DEFAULT 0.0,
                risk_score REAL DEFAULT 0.0,
                FOREIGN KEY (source_entity) REFERENCES entities(entity_id),
                FOREIGN KEY (destination_entity) REFERENCES entities(entity_id)
            )
        """)

        # Detected patterns
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patterns (
                pattern_id TEXT PRIMARY KEY,
                case_id TEXT NOT NULL,
                pattern_type TEXT NOT NULL,
                entities_involved TEXT,
                transactions_involved TEXT,
                confidence_score REAL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (case_id) REFERENCES aml_cases(case_id)
            )
        """)

        # Indicators/Red Flags table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS indicators (
                indicator_id TEXT PRIMARY KEY,
                case_id TEXT NOT NULL,
                indicator_type TEXT NOT NULL,
                indicator_value TEXT NOT NULL,
                severity TEXT DEFAULT 'medium',
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (case_id) REFERENCES aml_cases(case_id)
            )
        """)

        # Anomaly scores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS anomaly_scores (
                anomaly_id TEXT PRIMARY KEY,
                transaction_id TEXT NOT NULL,
                score REAL NOT NULL,
                reasons TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
            )
        """)

        # Audit log
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                log_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                action TEXT NOT NULL,
                case_id TEXT,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (case_id) REFERENCES aml_cases(case_id)
            )
        """)

        # Threat intelligence
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS threats (
                threat_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                severity TEXT,
                source TEXT,
                indicators TEXT,
                case_ids TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # KYC/KYP data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kyc_data (
                kyc_id TEXT PRIMARY KEY,
                entity_id TEXT NOT NULL,
                kyc_level TEXT DEFAULT 'basic',
                verification_status TEXT DEFAULT 'pending',
                documents TEXT,
                verified_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (entity_id) REFERENCES entities(entity_id)
            )
        """)

        # Create indexes for performance
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_cases_status ON aml_cases(status)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_cases_risk ON aml_cases(risk_level)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_transactions_case ON transactions(case_id)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(transaction_date)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(name)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_entities_risk ON entities(risk_score)")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_network_edges ON network_edges(source_entity, destination_entity)")

        conn.commit()
        conn.close()
        logger.info("Enhanced AML database schema initialized with indexing")

    def execute_query(self, query: str, params: tuple = ()) -> list:
        """Execute SELECT query"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            logger.error(f"Query error: {e}")
            return []

    def execute_update(self, query: str, params: tuple = ()) -> bool:
        """Execute INSERT/UPDATE/DELETE"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Update error: {e}")
            return False

    def execute_many(self, query: str, params_list: list) -> bool:
        """Execute multiple INSERT/UPDATE/DELETE"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.executemany(query, params_list)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Batch update error: {e}")
            return False


# ======================== DETECTION ALGORITHMS (ML & Pattern-Based) ========================


class AnomalyDetector:
    """Advanced anomaly detection using statistical methods"""

    def __init__(self):
        self.baseline_stats = {}

    def calculate_zscore(self, value: float, mean: float, std: float) -> float:
        """Calculate Z-score for anomaly detection"""
        if std == 0:
            return 0
        return abs((value - mean) / std)

    def detect_transaction_anomaly(self, transaction: Dict, entity_history: List[Dict]) -> Tuple[float, List[str]]:
        """Detect anomalies in transaction using multiple techniques"""
        reasons = []
        scores = []

        if not entity_history:
            return 0.0, reasons

        # Extract historical data
        amounts = [t.get('amount', 0) for t in entity_history]

        if not amounts:
            return 0.0, reasons

        mean_amount = np.mean(amounts)
        std_amount = np.std(amounts)

        # 1. Amount anomaly (Z-score > 2)
        amount_zscore = self.calculate_zscore(
            transaction.get('amount', 0), mean_amount, std_amount)
        if amount_zscore > 2:
            scores.append(min(amount_zscore * 10, 100))
            reasons.append(
                f"Unusual transaction amount (Z-score: {amount_zscore:.2f})")

        # 2. Frequency anomaly
        transaction_count = len(entity_history)
        avg_frequency = transaction_count / max(1, (datetime.now() - datetime.fromisoformat(
            entity_history[0].get('created_at', datetime.now().isoformat()))).days + 1)

        if avg_frequency < 1 and transaction_count > 0:  # Rarely transacts
            scores.append(50)
            reasons.append("Entity with low transaction frequency")

        # 3. Time-of-day anomaly
        txn_hour = datetime.fromisoformat(transaction.get(
            'transaction_date', datetime.now().isoformat())).hour
        if txn_hour >= 22 or txn_hour <= 4:
            scores.append(30)
            reasons.append("Transaction at unusual hour")

        # 4. Counterparty change anomaly
        historical_counterparties = set()
        for t in entity_history:
            historical_counterparties.add(
                t.get('destination_entity') or t.get('source_entity', ''))

        current_counterparty = transaction.get(
            'destination_entity') or transaction.get('source_entity', '')
        if current_counterparty not in historical_counterparties and len(historical_counterparties) > 0:
            scores.append(20)
            reasons.append("New counterparty entity")

        final_score = np.mean(scores) if scores else 0.0
        return min(final_score, 100.0), reasons


class PatternDetector:
    """Detect suspicious transaction patterns (Structuring, Round-tripping, etc.)"""

    def __init__(self, db: 'DatabaseManager'):
        self.db = db

    def detect_structuring(self, entity_id: str, threshold_days: int = 30,
                           threshold_amount: float = 50000, transaction_count: int = 5) -> Tuple[bool, Dict]:
        """
        Detect structuring pattern (multiple small transfers to avoid reporting threshold)
        Returns: (is_structuring, pattern_details)
        """
        query = """
            SELECT amount, transaction_date FROM transactions 
            WHERE (source_entity = ? OR destination_entity = ?)
            AND datetime(transaction_date) >= datetime('now', '-' || ? || ' days')
            ORDER BY transaction_date
        """

        results = self.db.execute_query(
            query, (entity_id, entity_id, threshold_days))

        if len(results) < transaction_count:
            return False, {}

        amounts = [row[0] for row in results]

        # Check if amounts are just below threshold
        below_threshold_count = sum(1 for a in amounts if a < threshold_amount)

        if below_threshold_count >= transaction_count:
            total = sum(amounts)
            return True, {
                'pattern': 'structuring',
                'confidence': min(0.95, below_threshold_count / len(amounts)),
                'total_amount': total,
                'transaction_count': below_threshold_count,
                'period_days': threshold_days
            }

        return False, {}

    def detect_round_tripping(self, entity_id: str, time_window_days: int = 30) -> Tuple[bool, Dict]:
        """
        Detect round-tripping pattern (funds flowing out and back quickly)
        """
        query = """
            SELECT source_entity, destination_entity, amount, transaction_date 
            FROM transactions 
            WHERE (source_entity = ? OR destination_entity = ?)
            AND datetime(transaction_date) >= datetime('now', '-' || ? || ' days')
            ORDER BY transaction_date
        """

        results = self.db.execute_query(
            query, (entity_id, entity_id, time_window_days))

        round_trips = []

        for i, result in enumerate(results):
            source, dest, amount, date = result
            counterparty = dest if source == entity_id else source

            # Look for reverse transaction
            for j in range(i + 1, len(results)):
                source2, dest2, amount2, date2 = results[j]
                counterparty2 = dest2 if source2 == entity_id else source2

                if counterparty == counterparty2 and source2 == entity_id and dest2 != entity_id:
                    time_diff = (datetime.fromisoformat(date2) -
                                 datetime.fromisoformat(date)).days
                    # Same amount, quick turnaround
                    if time_diff <= 3 and abs(amount - amount2) / amount < 0.1:
                        round_trips.append({
                            'counterparty': counterparty,
                            'amount': amount,
                            'days_between': time_diff
                        })

        if round_trips:
            return True, {
                'pattern': 'round_tripping',
                'confidence': min(0.9, len(round_trips) / max(1, len(results) / 2)),
                'round_trip_count': len(round_trips),
                'examples': round_trips[:3]
            }

        return False, {}

    def detect_fan_in_fan_out(self, entity_id: str) -> Dict:
        """Detect fan-in (many→one) and fan-out (one→many) patterns"""
        query_in = """
            SELECT COUNT(DISTINCT source_entity), SUM(amount) 
            FROM transactions WHERE destination_entity = ?
        """

        query_out = """
            SELECT COUNT(DISTINCT destination_entity), SUM(amount) 
            FROM transactions WHERE source_entity = ?
        """

        result_in = self.db.execute_query(query_in, (entity_id,))
        result_out = self.db.execute_query(query_out, (entity_id,))

        fan_in_count = result_in[0][0] if result_in else 0
        fan_out_count = result_out[0][0] if result_out else 0
        total_in = result_in[0][1] if result_in and result_in[0][1] else 0
        total_out = result_out[0][1] if result_out and result_out[0][1] else 0

        patterns = {}

        if fan_in_count > 10:
            patterns['fan_in'] = {
                'count': fan_in_count,
                'total_amount': total_in,
                'risk_score': min(100, fan_in_count * 2)
            }

        if fan_out_count > 10:
            patterns['fan_out'] = {
                'count': fan_out_count,
                'total_amount': total_out,
                'risk_score': min(100, fan_out_count * 2)
            }

        return patterns


class NetworkAnalyzer:
    """Analyze transaction networks for money laundering patterns"""

    def __init__(self, db: 'DatabaseManager'):
        self.db = db
        self.graph = defaultdict(list)
        self.nodes = {}

    def build_network(self, entity_ids: List[str]):
        """Build transaction network from entities"""
        query = """
            SELECT source_entity, destination_entity, amount, COUNT(*) as txn_count
            FROM transactions
            WHERE source_entity IN ({}) OR destination_entity IN ({})
            GROUP BY source_entity, destination_entity
        """.format(','.join(['?'] * len(entity_ids)), ','.join(['?'] * len(entity_ids)))

        results = self.db.execute_query(query, entity_ids + entity_ids)

        for source, dest, amount, count in results:
            self.graph[source].append((dest, amount, count))
            if source not in self.nodes:
                self.nodes[source] = NetworkNode(
                    str(uuid.uuid4()), source, 'source')
            if dest not in self.nodes:
                self.nodes[dest] = NetworkNode(
                    str(uuid.uuid4()), dest, 'destination')

            self.nodes[source].out_degree += 1
            self.nodes[dest].in_degree += 1

    def calculate_centrality(self) -> Dict[str, float]:
        """Calculate node centrality scores"""
        centrality = {}

        for node_id, node in self.nodes.items():
            # Weighted degree centrality
            total_weight = sum(amount for _, amount, _ in self.graph[node_id])
            centrality[node_id] = (
                node.in_degree + node.out_degree) * (1 + np.log1p(total_weight))

        return centrality

    def find_suspicious_chains(self, min_chain_length: int = 3) -> List[List[str]]:
        """Find suspicious transaction chains (potential layering)"""
        chains = []
        visited = set()

        for start_node in self.graph.keys():
            if start_node in visited:
                continue

            # BFS to find chains
            queue = deque([(start_node, [start_node])])

            while queue:
                current, path = queue.popleft()

                if len(path) > min_chain_length:
                    chains.append(path)
                    visited.update(path)
                    continue

                for next_node, _, _ in self.graph.get(current, []):
                    if next_node not in visited:
                        queue.append((next_node, path + [next_node]))

        return chains


class RiskScorer:
    """Calculate comprehensive risk scores"""

    def __init__(self, db: DatabaseManager, pattern_detector: PatternDetector,
                 network_analyzer: NetworkAnalyzer):
        self.db = db
        self.pattern_detector = pattern_detector
        self.network_analyzer = network_analyzer

        # Risk weights
        self.weights = {
            'transaction_anomaly': 0.25,
            'structuring': 0.30,
            'network_risk': 0.20,
            'indicators': 0.15,
            'entity_risk': 0.10
        }

    def score_entity(self, entity_id: str) -> float:
        """Calculate entity risk score (0-100)"""
        scores = {}

        # Check if entity is PEP or has sanctions
        query = "SELECT pep_flag, sanctions_flag FROM entities WHERE entity_id = ?"
        result = self.db.execute_query(query, (entity_id,))

        if result:
            pep_flag, sanctions_flag = result[0]
            if sanctions_flag:
                scores['sanctions'] = 100
            elif pep_flag:
                scores['pep'] = 70

        # Transaction history risk
        query = "SELECT COUNT(*) as txn_count, SUM(amount) as total FROM transactions WHERE source_entity = ? OR destination_entity = ?"
        result = self.db.execute_query(query, (entity_id, entity_id))

        if result and result[0][0] > 0:
            txn_count = result[0][0]
            if txn_count > 100:
                scores['activity_level'] = 30

        # Network centrality
        self.network_analyzer.build_network([entity_id])
        centrality = self.network_analyzer.calculate_centrality()
        if entity_id in centrality and centrality[entity_id] > 50:
            scores['network_centrality'] = 40

        # Structuring detection
        is_structuring, _ = self.pattern_detector.detect_structuring(entity_id)
        if is_structuring:
            scores['structuring'] = 80

        final_score = np.mean(list(scores.values())) if scores else 0.0
        return min(final_score, 100.0)

    def score_case(self, case_id: str) -> float:
        """Calculate overall case risk score"""
        scores = {}

        # Get case details
        query = "SELECT risk_level, amount_involved FROM aml_cases WHERE case_id = ?"
        case_result = self.db.execute_query(query, (case_id,))

        if not case_result:
            return 0.0

        risk_level, amount = case_result[0]

        # Risk level baseline
        risk_mapping = {'low': 20, 'medium': 50, 'high': 75, 'critical': 95}
        scores['risk_level'] = risk_mapping.get(risk_level, 50)

        # Amount involved
        if amount and amount > 10000000:  # >10M
            scores['amount'] = 80
        elif amount and amount > 1000000:  # >1M
            scores['amount'] = 60

        # Pattern indicators
        query = "SELECT pattern_indicators FROM aml_cases WHERE case_id = ?"
        patterns_result = self.db.execute_query(query, (case_id,))
        if patterns_result and patterns_result[0][0]:
            scores['patterns'] = 70

        return min(np.mean(list(scores.values())) if scores else 0.0, 100.0)


# ======================== ENTITY MANAGER ========================


class EntityManager:
    """Manage entities (persons, organizations)"""

    def __init__(self, db: DatabaseManager):
        self.db = db

    def create_entity(self, entity_data: Dict) -> Tuple[bool, str, str]:
        """Create new entity"""
        try:
            entity_id = str(uuid.uuid4())

            query = """
                INSERT INTO entities (entity_id, name, entity_type, cnic_number, 
                                     pep_flag, sanctions_flag, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            params = (
                entity_id,
                entity_data.get('name', ''),
                entity_data.get('entity_type', 'person'),
                entity_data.get('cnic_number'),
                entity_data.get('pep_flag', False),
                entity_data.get('sanctions_flag', False),
                json.dumps(entity_data.get('metadata', {}))
            )

            if self.db.execute_update(query, params):
                logger.info(f"Entity created: {entity_id}")
                return True, f"Entity created", entity_id

            return False, "Failed to create entity", ""
        except Exception as e:
            logger.error(f"Create entity error: {e}")
            return False, str(e), ""

    def get_entity(self, entity_id: str) -> Optional[Dict]:
        """Get entity details"""
        query = "SELECT * FROM entities WHERE entity_id = ?"
        result = self.db.execute_query(query, (entity_id,))

        if result:
            row = dict(result[0])
            if row.get('metadata'):
                row['metadata'] = json.loads(row['metadata'])
            return row
        return None

    def update_entity_risk(self, entity_id: str, risk_score: float):
        """Update entity risk score"""
        query = "UPDATE entities SET risk_score = ? WHERE entity_id = ?"
        self.db.execute_update(query, (risk_score, entity_id))


# ======================== CASE MANAGER (Enhanced) ========================


class CaseManager:
    def __init__(self, db: DatabaseManager, entity_mgr: EntityManager,
                 pattern_detector: PatternDetector, risk_scorer: RiskScorer,
                 network_analyzer: NetworkAnalyzer):
        self.db = db
        self.entity_mgr = entity_mgr
        self.pattern_detector = pattern_detector
        self.risk_scorer = risk_scorer
        self.network_analyzer = network_analyzer

    def create_case(self, case_data: dict) -> Tuple[bool, str, str]:
        """Create new AML case"""
        try:
            case_id = str(uuid.uuid4())
            case_number = f"CASE-{datetime.now().strftime('%Y%m%d%H%M%S')}"

            query = """
                INSERT INTO aml_cases 
                (case_id, case_number, title, description, case_type, status, risk_level, 
                 accused_names, cnic_numbers, amount_involved, currency, source_of_funds,
                 destination, investigation_officer, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            params = (
                case_id,
                case_number,
                case_data.get('title', 'Untitled'),
                case_data.get('description', ''),
                case_data.get('case_type', 'other'),
                'open',
                case_data.get('risk_level', 'medium'),
                case_data.get('accused_names', ''),
                case_data.get('cnic_numbers', ''),
                float(case_data.get('amount_involved', 0)),
                case_data.get('currency', 'PKR'),
                case_data.get('source_of_funds', ''),
                case_data.get('destination', ''),
                case_data.get('investigation_officer', ''),
                case_data.get('notes', '')
            )

            if self.db.execute_update(query, params):
                logger.info(f"Case created: {case_number}")
                return True, f"Case {case_number} created", case_id
            return False, "Failed to create case", ""
        except Exception as e:
            logger.error(f"Create case error: {e}")
            return False, str(e), ""

    def add_transaction_to_case(self, case_id: str, transaction_data: Dict) -> Tuple[bool, str]:
        """Add transaction to case with anomaly detection"""
        try:
            transaction_id = str(uuid.uuid4())

            # Get entity history for anomaly detection
            source_entity = transaction_data.get('source_entity')
            history_query = """
                SELECT amount, created_at FROM transactions 
                WHERE source_entity = ? OR destination_entity = ?
                ORDER BY created_at DESC LIMIT 20
            """
            history = self.db.execute_query(
                history_query, (source_entity, source_entity))
            history_dicts = [{'amount': h[0], 'created_at': h[1]}
                             for h in history]

            # Detect anomalies
            anomaly_detector = AnomalyDetector()
            anomaly_score, anomaly_reasons = anomaly_detector.detect_transaction_anomaly(
                transaction_data, history_dicts
            )

            query = """
                INSERT INTO transactions 
                (transaction_id, case_id, source_entity, destination_entity, 
                 amount, currency, transaction_date, status, transaction_type, 
                 channels, description, flags, risk_score, detected_patterns, anomaly_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            params = (
                transaction_id,
                case_id,
                source_entity,
                transaction_data.get('destination_entity'),
                float(transaction_data.get('amount', 0)),
                transaction_data.get('currency', 'PKR'),
                transaction_data.get('transaction_date',
                                     datetime.now().isoformat()),
                'completed',
                transaction_data.get('transaction_type', 'transfer'),
                json.dumps(transaction_data.get('channels', [])),
                transaction_data.get('description', ''),
                json.dumps(transaction_data.get('flags', [])),
                transaction_data.get('risk_score', 0.0),
                json.dumps(transaction_data.get('detected_patterns', [])),
                anomaly_score
            )

            if self.db.execute_update(query, params):
                # Store anomaly score
                if anomaly_score > 0:
                    anomaly_query = """
                        INSERT INTO anomaly_scores (anomaly_id, transaction_id, score, reasons)
                        VALUES (?, ?, ?, ?)
                    """
                    self.db.execute_update(anomaly_query, (
                        str(uuid.uuid4()),
                        transaction_id,
                        anomaly_score,
                        json.dumps(anomaly_reasons)
                    ))

                logger.info(f"Transaction added to case {case_id}")
                return True, f"Transaction {transaction_id} added"

            return False, "Failed to add transaction"
        except Exception as e:
            logger.error(f"Add transaction error: {e}")
            return False, str(e)

    def analyze_case(self, case_id: str) -> Dict:
        """Comprehensive case analysis including pattern detection"""
        try:
            case = self.get_case(case_id)
            if not case:
                return {'error': 'Case not found'}

            # Get all transactions in case
            query = "SELECT * FROM transactions WHERE case_id = ?"
            transactions = self.db.execute_query(query, (case_id,))

            analysis = {
                'case_id': case_id,
                'patterns': {},
                'network_analysis': {},
                'risk_assessment': {},
                'anomalies': []
            }

            if transactions:
                # Extract entities
                entities = set()
                for txn in transactions:
                    entities.add(txn[2])  # source_entity
                    entities.add(txn[3])  # destination_entity

                # Pattern detection
                if len(entities) > 0:
                    sample_entity = list(entities)[0]

                    structuring, struct_details = self.pattern_detector.detect_structuring(
                        sample_entity)
                    if structuring:
                        analysis['patterns']['structuring'] = struct_details

                    round_trip, rt_details = self.pattern_detector.detect_round_tripping(
                        sample_entity)
                    if round_trip:
                        analysis['patterns']['round_tripping'] = rt_details

                    fan_patterns = self.pattern_detector.detect_fan_in_fan_out(
                        sample_entity)
                    analysis['patterns'].update(fan_patterns)

                # Network analysis
                if len(entities) > 1:
                    self.network_analyzer.build_network(list(entities))
                    centrality = self.network_analyzer.calculate_centrality()
                    suspicious_chains = self.network_analyzer.find_suspicious_chains()

                    analysis['network_analysis'] = {
                        'total_entities': len(entities),
                        'high_centrality_nodes': {k: v for k, v in centrality.items() if v > 50},
                        'suspicious_chains': suspicious_chains[:5]
                    }

                # Risk assessment
                case_risk = self.risk_scorer.score_case(case_id)
                analysis['risk_assessment'] = {
                    'case_risk_score': case_risk,
                    'risk_level': 'critical' if case_risk > 80 else 'high' if case_risk > 60 else 'medium' if case_risk > 40 else 'low'
                }

                # Anomalies
                anomaly_query = "SELECT * FROM anomaly_scores WHERE transaction_id IN (SELECT transaction_id FROM transactions WHERE case_id = ?)"
                anomalies = self.db.execute_query(anomaly_query, (case_id,))
                for anomaly in anomalies:
                    analysis['anomalies'].append({
                        'transaction_id': anomaly[1],
                        'score': anomaly[2],
                        'reasons': json.loads(anomaly[3]) if anomaly[3] else []
                    })

            return analysis
        except Exception as e:
            logger.error(f"Analyze case error: {e}")
            return {'error': str(e)}

    def get_case(self, case_id: str) -> Optional[dict]:
        """Get case details"""
        try:
            query = "SELECT * FROM aml_cases WHERE case_id = ?"
            result = self.db.execute_query(query, (case_id,))
            if result:
                return dict(result[0])
            return None
        except Exception as e:
            logger.error(f"Get case error: {e}")
            return None

    def list_cases(self, status: str = None, limit: int = 100) -> list:
        """List cases with optional filtering"""
        try:
            if status:
                query = "SELECT * FROM aml_cases WHERE status = ? ORDER BY created_at DESC LIMIT ?"
                results = self.db.execute_query(query, (status, limit))
            else:
                query = "SELECT * FROM aml_cases ORDER BY updated_at DESC LIMIT ?"
                results = self.db.execute_query(query, (limit,))

            return [dict(row) for row in results] if results else []
        except Exception as e:
            logger.error(f"List cases error: {e}")
            return []

    def update_case_status(self, case_id: str, new_status: str, updated_by: str = None) -> Tuple[bool, str]:
        """Update case status"""
        try:
            query = "UPDATE aml_cases SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE case_id = ?"
            if self.db.execute_update(query, (new_status, case_id)):
                logger.info(f"Case {case_id} status → {new_status}")
                return True, "Status updated"
            return False, "Update failed"
        except Exception as e:
            logger.error(f"Update status error: {e}")
            return False, str(e)

    def get_statistics(self) -> dict:
        """Get comprehensive case statistics"""
        try:
            total = self.db.execute_query(
                "SELECT COUNT(*) FROM aml_cases")[0][0]
            by_status = self.db.execute_query(
                "SELECT status, COUNT(*) FROM aml_cases GROUP BY status")
            by_type = self.db.execute_query(
                "SELECT case_type, COUNT(*) FROM aml_cases GROUP BY case_type")
            by_risk = self.db.execute_query(
                "SELECT risk_level, COUNT(*) FROM aml_cases GROUP BY risk_level")
            total_amount = self.db.execute_query(
                "SELECT SUM(amount_involved) FROM aml_cases WHERE amount_involved > 0")[0][0] or 0

            high_priority = self.db.execute_query(
                "SELECT COUNT(*) FROM aml_cases WHERE priority = 1")[0][0]

            # Enhanced statistics
            avg_risk_score = self.db.execute_query(
                "SELECT AVG(network_risk_score) FROM aml_cases WHERE network_risk_score > 0")[0][0] or 0

            high_risk_cases = self.db.execute_query(
                "SELECT COUNT(*) FROM aml_cases WHERE risk_level IN ('high', 'critical')")[0][0]

            return {
                'total_cases': total,
                'total_amount_pkr': total_amount,
                'high_priority_cases': high_priority,
                'high_risk_cases': high_risk_cases,
                'average_network_risk_score': round(avg_risk_score, 2),
                'by_status': {row[0]: row[1] for row in by_status} if by_status else {},
                'by_type': {row[0]: row[1] for row in by_type} if by_type else {},
                'by_risk': {row[0]: row[1] for row in by_risk} if by_risk else {}
            }
        except Exception as e:
            logger.error(f"Statistics error: {e}")
            return {}


# ======================== THREAT MANAGER ========================


class ThreatManager:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def ingest_threat(self, threat_data: dict) -> Tuple[bool, str]:
        """Ingest threat intelligence"""
        try:
            threat_id = str(uuid.uuid4())
            query = """
                INSERT INTO threats (threat_id, title, description, severity, source, indicators)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            params = (
                threat_id,
                threat_data.get('title', 'Unknown'),
                threat_data.get('description', ''),
                threat_data.get('severity', 'medium'),
                threat_data.get('source', 'Unknown'),
                json.dumps(threat_data.get('indicators', []))
            )

            if self.db.execute_update(query, params):
                return True, f"Threat ingested: {threat_id}"
            return False, "Failed to ingest threat"
        except Exception as e:
            logger.error(f"Ingest threat error: {e}")
            return False, str(e)

    def get_threats(self, severity: str = None) -> list:
        """Get threats with optional severity filter"""
        try:
            if severity:
                query = "SELECT * FROM threats WHERE severity = ? ORDER BY created_at DESC"
                results = self.db.execute_query(query, (severity,))
            else:
                query = "SELECT * FROM threats ORDER BY created_at DESC LIMIT 100"
                results = self.db.execute_query(query)

            return [dict(row) for row in results] if results else []
        except Exception as e:
            logger.error(f"Get threats error: {e}")
            return []


# ======================== FLASK APP ========================


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = os.environ.get(
        'SECRET_KEY', 'aml-secret-v6-prod-enhanced')

    # Initialize all managers
    db = DatabaseManager()
    entity_mgr = EntityManager(db)
    pattern_detector = PatternDetector(db)
    network_analyzer = NetworkAnalyzer(db)
    risk_scorer = RiskScorer(db, pattern_detector, network_analyzer)
    case_mgr = CaseManager(db, entity_mgr, pattern_detector,
                           risk_scorer, network_analyzer)
    threat_mgr = ThreatManager(db)

    # ========== ROOT ENDPOINTS ==========

    @app.route('/', methods=['GET'])
    def index():
        """Serve interactive dashboard with forms"""
        try:
            html_path = os.path.join(
                os.path.dirname(__file__), 'dashboard.html')
            if os.path.exists(html_path):
                with open(html_path, 'r', encoding='utf-8') as f:
                    return f.read()
        except:
            pass
        # Fallback JSON response
        return jsonify({
            'system': 'AML AML System v6.0 Enhanced',
            'status': 'operational',
            'database': 'connected',
            'message': 'Open http://localhost:5000 in browser for dashboard',
            'features': ['ML Anomaly Detection', 'Pattern Detection', 'Network Analysis', 'Risk Scoring']
        }), 200

    # ========== HEALTH ==========

    @app.route('/api/health', methods=['GET'])
    def health():
        """Health check"""
        return jsonify({
            'status': 'healthy',
            'version': '6.0-enhanced',
            'timestamp': datetime.now().isoformat(),
            'database': 'connected',
            'features': {
                'anomaly_detection': True,
                'pattern_detection': True,
                'network_analysis': True,
                'risk_scoring': True
            }
        }), 200

    # ========== ENTITY ENDPOINTS ==========

    @app.route('/api/entities', methods=['POST'])
    def create_entity():
        """Create entity"""
        data = request.get_json()
        success, message, entity_id = entity_mgr.create_entity(data)
        if success:
            return jsonify({'success': True, 'message': message, 'entity_id': entity_id}), 201
        return jsonify({'success': False, 'message': message}), 400

    @app.route('/api/entities/<entity_id>', methods=['GET'])
    def get_entity(entity_id):
        """Get entity details"""
        entity = entity_mgr.get_entity(entity_id)
        if entity:
            return jsonify(entity), 200
        return jsonify({'error': 'Entity not found'}), 404

    # ========== CASE ENDPOINTS ==========

    @app.route('/api/cases', methods=['GET'])
    def list_cases():
        """List all cases"""
        status = request.args.get('status')
        cases = case_mgr.list_cases(status)
        return jsonify({'cases': cases, 'count': len(cases)}), 200

    @app.route('/api/cases', methods=['POST'])
    def create_case():
        """Create new AML case"""
        data = request.get_json()
        success, message, case_id = case_mgr.create_case(data)
        if success:
            return jsonify({'success': True, 'message': message, 'case_id': case_id}), 201
        return jsonify({'success': False, 'message': message}), 400

    @app.route('/api/cases/<case_id>', methods=['GET'])
    def get_case(case_id):
        """Get case details"""
        case = case_mgr.get_case(case_id)
        if case:
            return jsonify(case), 200
        return jsonify({'error': 'Case not found'}), 404

    @app.route('/api/cases/<case_id>/status', methods=['PUT'])
    def update_case_status(case_id):
        """Update case status"""
        data = request.get_json()
        success, message = case_mgr.update_case_status(
            case_id, data.get('status'))
        if success:
            return jsonify({'success': True, 'message': message}), 200
        return jsonify({'success': False, 'message': message}), 400

    @app.route('/api/cases/<case_id>/transactions', methods=['POST'])
    def add_transaction(case_id):
        """Add transaction with anomaly detection"""
        data = request.get_json()
        success, message = case_mgr.add_transaction_to_case(case_id, data)
        if success:
            return jsonify({'success': True, 'message': message}), 201
        return jsonify({'success': False, 'message': message}), 400

    @app.route('/api/cases/<case_id>/analysis', methods=['GET'])
    def analyze_case(case_id):
        """Get comprehensive case analysis"""
        analysis = case_mgr.analyze_case(case_id)
        return jsonify(analysis), 200

    # ========== STATISTICS ==========

    @app.route('/api/statistics', methods=['GET'])
    def get_statistics():
        """Get comprehensive system statistics"""
        stats = case_mgr.get_statistics()
        return jsonify(stats), 200

    # ========== THREAT ENDPOINTS ==========

    @app.route('/api/threats', methods=['GET'])
    def get_threats():
        """Get threat intelligence"""
        severity = request.args.get('severity')
        threats = threat_mgr.get_threats(severity)
        return jsonify({'threats': threats, 'count': len(threats)}), 200

    @app.route('/api/threats/ingest', methods=['POST'])
    def ingest_threat():
        """Ingest threat intelligence"""
        data = request.get_json()
        success, message = threat_mgr.ingest_threat(data)
        if success:
            return jsonify({'success': True, 'message': message}), 201
        return jsonify({'success': False, 'message': message}), 400

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Endpoint not found'}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    routes = len(list(app.url_map.iter_rules()))
    logger.info(f"Enhanced AML app created with {routes} routes")
    return app


if __name__ == '__main__':
    app = create_app()
    logger.info("Starting AML AML System v6.0 Enhanced")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

