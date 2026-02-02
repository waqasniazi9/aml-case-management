# Solana Token ACL Integration Guide

## Overview

The FIA AML Case Management System v3.5 now integrates **Solana Token ACL (Access Control List)** capabilities based on the sRFC 37 standard. This enables cryptocurrency compliance monitoring by linking Solana blockchain wallets and token accounts to AML investigations.

## Architecture

### Components

1. **SolanaACLManager** - Manages wallet registration, ACL configuration, and compliance status
2. **TokenACLComplianceEngine** - Analyzes token transfers and detects suspicious patterns
3. **Database Layer** - 5 new tables for Solana integration:
   - `solana_wallets` - Registered wallets with KYC/compliance status
   - `token_accounts` - Token accounts linked to wallets
   - `token_acl_config` - ACL configuration per token mint
   - `acl_transactions` - Transaction history and compliance records

### Data Models

#### SolanaWallet

```python
{
    "address": "Base58_encoded_address",
    "owner_name": "Wallet owner name",
    "kyc_status": true/false,
    "aml_case_id": "UUID of linked AML case",
    "is_whitelisted": true/false,
    "is_blacklisted": true/false
}
```

#### TokenAccount

```python
{
    "account_address": "Base58_encoded_account",
    "owner_address": "Base58_encoded_owner",
    "is_frozen": true/false,
    "acl_status": "COMPLIANT|NON_COMPLIANT|FROZEN|THAWED|PENDING|FLAGGED",
    "list_type": "WHITELIST|BLACKLIST|NONE",
    "associated_case_id": "UUID of linked AML case"
}
```

#### TokenACLConfig

```python
{
    "mint_address": "Base58_encoded_mint",
    "gate_program": "Gate program address",
    "authority_pubkey": "Authority public key",
    "list_type": "WHITELIST|BLACKLIST",
    "permissionless_freeze": true/false,
    "permissionless_thaw": true/false,
    "associated_case_id": "UUID of linked AML case"
}
```

#### ACLTransaction

```python
{
    "transaction_hash": "Solana transaction signature",
    "action_type": "FREEZE|THAW|TRANSFER",
    "wallet_address": "Base58_encoded_wallet",
    "token_account": "Base58_encoded_token_account",
    "compliance_status": "COMPLIANT|NON_COMPLIANT|PENDING|FLAGGED",
    "associated_case_id": "UUID of linked AML case"
}
```

## API Endpoints

### Wallet Management

#### Register Solana Wallet

```http
POST /api/solana/wallet/register
Content-Type: application/json

{
    "address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "owner_name": "John Doe",
    "kyc_status": true,
    "aml_case_id": "case-uuid-123",
    "is_whitelisted": true,
    "is_blacklisted": false
}
```

**Response (201):**

```json
{
    "success": true,
    "message": "Wallet registered successfully",
    "wallet_id": "wallet-uuid-123"
}
```

#### Get Wallet Summary

```http
GET /api/solana/wallet/{wallet_address}
```

**Response (200):**

```json
{
    "success": true,
    "wallet": {
        "id": "wallet-uuid",
        "address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "owner_name": "John Doe",
        "kyc_status": true,
        "is_whitelisted": true,
        "is_blacklisted": false,
        "aml_case_id": "case-uuid-123",
        "registered_date": "2024-01-15T10:30:00",
        "compliance_score": 85
    }
}
```

#### Check Wallet Compliance

```http
GET /api/solana/wallet/{wallet_address}/compliance
```

**Response (200):**

```json
{
    "success": true,
    "wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "compliance": {
        "compliant": true,
        "whitelisted": true,
        "kyc_verified": true,
        "reason": "Wallet passes compliance checks"
    }
}
```

#### Update Wallet Compliance

```http
PUT /api/solana/wallet/{wallet_address}/compliance
Content-Type: application/json

{
    "is_whitelisted": true,
    "is_blacklisted": false,
    "kyc_status": true
}
```

**Response (200):**

```json
{
    "success": true,
    "message": "Wallet compliance updated successfully"
}
```

### Token Account Management

#### Add Token Account

```http
POST /api/solana/token-account
Content-Type: application/json

{
    "account_address": "ATokenGPvbdGVqstok2z6cBvAm8fWzD21qQvEYh7PzAr",
    "owner_address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "is_frozen": false,
    "acl_status": "COMPLIANT",
    "list_type": "WHITELIST",
    "associated_case_id": "case-uuid-123"
}
```

**Response (201):**

```json
{
    "success": true,
    "message": "Token account registered successfully"
}
```

### ACL Configuration

#### Configure Token ACL

```http
POST /api/solana/acl/configure
Content-Type: application/json

{
    "mint_address": "EPjFWaJwqNog3jFfSo0ggUkh2B8ZwQEoR1ZcMV9B534m",
    "gate_program": "GateProgramAddress...",
    "authority_pubkey": "AuthorityPubKeyAddress...",
    "list_type": "WHITELIST",
    "permissionless_freeze": false,
    "permissionless_thaw": false,
    "associated_case_id": "case-uuid-123"
}
```

**Response (201):**

```json
{
    "success": true,
    "message": "ACL configuration saved successfully"
}
```

### Transaction Recording

#### Record ACL Transaction

```http
POST /api/solana/acl/transaction
Content-Type: application/json

{
    "transaction_hash": "5vWEYLnTa3gN8qE7hFkC8mP...",
    "action_type": "FREEZE",
    "wallet_address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "token_account": "ATokenGPvbdGVqstok2z6cBvAm8fWzD21qQvEYh7PzAr",
    "compliance_status": "COMPLIANT",
    "associated_case_id": "case-uuid-123"
}
```

**Response (201):**

```json
{
    "success": true,
    "message": "Transaction recorded successfully"
}
```

### Compliance Analysis

#### Analyze Token Transfer

```http
POST /api/solana/transfer/analyze
Content-Type: application/json

{
    "from_wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "to_wallet": "AnotherWalletAddress...",
    "amount": 1000000,
    "token_mint": "EPjFWaJwqNog3jFfSo0ggUkh2B8ZwQEoR1ZcMV9B534m"
}
```

**Response (200):**

```json
{
    "success": true,
    "analysis": {
        "transfer_id": "analysis-uuid",
        "from_wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "to_wallet": "AnotherWalletAddress...",
        "amount": 1000000,
        "compliant": true,
        "violations": [],
        "recommendations": []
    }
}
```

#### Detect Suspicious Patterns

```http
GET /api/solana/patterns/detect/{wallet_address}?hours=24
```

**Response (200):**

```json
{
    "success": true,
    "patterns": {
        "wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "time_window_hours": 24,
        "suspicious": false,
        "flags": []
    }
}
```

### Dashboard & Analytics

#### Solana Token ACL Dashboard

```http
GET /api/solana/dashboard
```

**Response (200):**

```json
{
    "success": true,
    "dashboard": {
        "registered_wallets": 42,
        "compliant_wallets": 38,
        "flagged_wallets": 4,
        "recent_transactions": 156,
        "whitelist_tokens": 12,
        "blacklist_tokens": 3
    }
}
```

## Compliance Workflow

### 1. Register Wallet

When a wallet is linked to an AML case:

```bash
POST /api/solana/wallet/register
{
    "address": "wallet_address",
    "owner_name": "Suspect name",
    "kyc_status": false,
    "aml_case_id": "case_uuid"
}
```

### 2. Verify KYC

Once KYC is completed:

```bash
PUT /api/solana/wallet/{wallet_address}/compliance
{
    "kyc_status": true
}
```

### 3. Configure ACL

Set up access control rules for tokens:

```bash
POST /api/solana/acl/configure
{
    "mint_address": "token_mint",
    "list_type": "WHITELIST",
    "associated_case_id": "case_uuid"
}
```

### 4. Monitor Transfers

Analyze each transaction for compliance:

```bash
POST /api/solana/transfer/analyze
{
    "from_wallet": "sender",
    "to_wallet": "receiver",
    "token_mint": "token"
}
```

### 5. Record Actions

Track freeze/thaw events:

```bash
POST /api/solana/acl/transaction
{
    "transaction_hash": "tx_hash",
    "action_type": "FREEZE",
    "compliance_status": "COMPLIANT"
}
```

## Compliance Scoring

**Compliance Score Calculation:**

- Base score: 50
- +20: KYC status verified
- +15: Whitelisted wallet
- -40: Blacklisted wallet
- Range: 0-100

**Risk Levels Based on Compliance:**

- **Compliant** (Score 80-100): Green - Low risk
- **Monitored** (Score 60-79): Yellow - Medium risk
- **Flagged** (Score 40-59): Orange - High risk
- **Blocked** (Score 0-39): Red - Critical risk

## Error Handling

All endpoints return error responses in this format:

```json
{
    "success": false,
    "message": "Error description"
}
```

**Common HTTP Status Codes:**

- 200: Success
- 201: Created
- 400: Invalid request
- 404: Not found
- 500: Server error

## Integration with AML Cases

All Solana wallets and token accounts can be linked to AML cases via the `associated_case_id` field. This enables:

1. **Case-linked monitoring** - All wallet activity tracked in case context
2. **Integrated reporting** - Solana transactions included in case reports
3. **Compliance evidence** - Transaction history linked to investigation timeline
4. **Pattern analysis** - Cross-reference blockchain activity with traditional financial data

## Security Considerations

1. **Base58 Validation** - All Solana addresses are validated before storage
2. **Audit Logging** - All operations logged with timestamps
3. **Compliance Status** - Prevents transactions from non-compliant wallets
4. **Case Linking** - Enforces relationship between wallets and investigations
5. **Transaction History** - Immutable record of all compliance actions

## Example Usage

### Scenario: Investigating Suspicious Crypto Transfers

1. **Create AML Case**

   ```bash
   POST /api/cases
   {
       "accused_name": "Ali Khan",
       "investigation_type": "Crypto Money Laundering"
   }
   ```

2. **Register Suspect's Wallet**

   ```bash
   POST /api/solana/wallet/register
   {
       "address": "SuspectWalletAddress",
       "owner_name": "Ali Khan",
       "kyc_status": false,
       "aml_case_id": "case_uuid"
   }
   ```

3. **Update Compliance After KYC**

   ```bash
   PUT /api/solana/wallet/{wallet_address}/compliance
   {
       "kyc_status": true,
       "is_whitelisted": false
   }
   ```

4. **Monitor Large Transfer**

   ```bash
   POST /api/solana/transfer/analyze
   {
       "from_wallet": "SuspectWalletAddress",
       "to_wallet": "ReceiverWalletAddress",
       "amount": 50000000000,
       "token_mint": "USDCMint"
   }
   ```

5. **Check Dashboard**

   ```bash
   GET /api/solana/dashboard
   ```

## Version Information

- **System Version**: 3.5
- **Solana Integration Version**: 1.0
- **Standard**: sRFC 37 Token ACL
- **Python Version**: 3.8+
- **Key Dependency**: base58==2.1.1

## Support & Documentation

For more information:

- See [README.md](README.md) for system overview
- See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for traditional AML endpoints
- Check audit logs for transaction history
