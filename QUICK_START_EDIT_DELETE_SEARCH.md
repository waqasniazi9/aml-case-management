# Quick Start - Edit/Delete/Search Features

## 🚀 Get Started in 30 Seconds

### Step 1: Open Your Dashboard

Navigate to: **<http://127.0.0.1:5000>**

### Step 2: Login

- Username: `admin` (or your username)
- Password: `admin123` (or your password)

### Step 3: Start Using New Features

---

## 📖 Feature Guides

### 🔍 Search Cases

**Location**: Cases Tab → "Your Cases" Section

**How to Search:**

1. Type in the search box: "🔍 Search cases by title, category, or ID..."
2. See results filter in real-time as you type
3. Clear the search box to see all cases

**Search Searches:**

- Case ID
- Case Title
- Category
- Accused Names

**Example:**

```
Search for: "fraud" → Shows all cases with "fraud" in title
Search for: "PKR 50000" → Shows high-value cases (if in ID)
```

---

### ✏️ Edit Cases

**Location**: Cases Tab → "Your Cases" Section → Action Column

**How to Edit:**

1. Find the case in the table
2. Click the **✏️ Edit** button on that row
3. **First Dialog**: Enter new Case Title, click OK
4. **Second Dialog**: Enter new Description, click OK
5. ✅ **Success!** Case updated and table refreshes

**Example Workflow:**

```
Current: Title = "Suspicious Transfer"
Edit → Enter "Suspicious Transfer - Updated"
Success notification appears
Table shows updated title
```

---

### 🗑️ Delete Cases

**Location**: Cases Tab → "Your Cases" Section → Action Column

**How to Delete:**

1. Find the case you want to delete
2. Click the **🗑️ Delete** button on that row
3. **Confirmation Dialog**: "Are you sure?" → Click OK to confirm
4. ✅ **Case Deleted!** Removed from table and database
5. **Undo not available** - Deletion is permanent

**⚠️ Warning:**

- This action CANNOT be undone
- Case is permanently deleted from database
- All related transactions and data remain (linked records)
- Audit trail logs the deletion with timestamp and user

---

### 📦 Transaction History

**Location**: Transactions Tab → "Transaction History" Section

**Features:**

- See all historical transactions in a table
- Shows: Case ID, Sender, Receiver, Amount, Date, Status
- Automatically loads when you log in
- Updates after adding new transactions

**Table Columns:**

| Column | Description |
|--------|-------------|
| Case ID | Which case the transaction belongs to |
| Sender | Who sent the money |
| Receiver | Who received the money |
| Amount | Transaction amount in PKR |
| Date | When transaction occurred |
| Status | completed, pending, failed, etc. |
| Actions | Delete button |

---

### 🔍 Search Transactions

**Location**: Transactions Tab → "Transaction History" → Search Box

**How to Search:**

1. Type in search box: "🔍 Search by sender, receiver, or case ID..."
2. Results filter in real-time
3. Clear box to see all transactions

**Search Searches:**

- Case ID
- Sender Name
- Receiver Name

**Example:**

```
Search for: "Ahmed" → Shows all transactions from/to Ahmed
Search for: "CASE-001" → Shows all transactions in that case
```

---

### 🗑️ Delete Transactions

**Location**: Transactions Tab → "Transaction History" → Action Column

**How to Delete:**

1. Find transaction in the table
2. Click **🗑️ Delete** button
3. **Confirmation Dialog** → Click OK to confirm
4. ✅ Transaction deleted from database
5. Table automatically refreshes

**⚠️ Warning:**

- Deletion is permanent
- Cannot be undone
- Audit log records deletion with timestamp and user

---

## 💡 Usage Tips & Tricks

### Search Tips

- **Case-insensitive**: Search for "FRAUD" or "fraud" - both work
- **Partial matches**: Type "sus" to find "Suspicious"
- **Multiple criteria**: Type "PKR 50000" to find transactions
- **Real-time**: See results as you type, no need to press Enter

### Edit Tips

- **Edit one field at a time**: First title, then description
- **Can't edit amount/category**: Only title and description editable
- **Success appears instantly**: Green notification at top-right
- **See changes immediately**: Table updates without page refresh

### Delete Tips

- **Always confirms first**: Prevents accidental deletion
- **Click Cancel to abort**: If you change your mind
- **Logged in audit trail**: Every deletion is tracked
- **Best practice**: Search first, then delete to be sure

### Action Column Tips

- **Edit button (✏️)**: Blue button - Click to modify
- **Delete button (🗑️)**: Red button - Click to remove
- **Both on same row**: Pick the action you need
- **Disabled during API calls**: Wait for response before next action

---

## 🎯 Common Scenarios

### Scenario 1: Find and Delete a Case

```
1. Go to Cases tab
2. Type case ID in search → Shows matching case
3. Click Delete button on that row
4. Confirm deletion
5. Case removed from database
```

### Scenario 2: Search for All Transactions from a Specific Sender

```
1. Go to Transactions tab
2. Scroll to "Transaction History"
3. Type sender name in search box
4. See all transactions filtered by that sender
5. Delete any transaction if needed
```

### Scenario 3: Update Multiple Cases

```
1. Go to Cases tab
2. Find first case
3. Click Edit → Update title/description
4. Click Edit again for next case
5. Repeat for each case needing updates
```

### Scenario 4: Clean Up Old Transactions

```
1. Go to Transactions tab
2. Search for old transaction by sender/receiver
3. Scroll through filtered results
4. Delete unwanted transactions one by one
5. Confirm each deletion
```

---

## ⚙️ Settings & Preferences

### Search Behavior

- **Auto-refresh**: Search updates automatically as you type
- **Case-sensitive**: No (searches are case-insensitive)
- **Partial matching**: Yes (doesn't require exact match)

### Edit Behavior

- **Field validation**: Basic input only (no format checking)
- **Character limit**: No hard limit
- **Special characters**: Allowed (use with care)

### Delete Behavior

- **Confirmation required**: Always (no bypass)
- **Recovery option**: None (permanent deletion)
- **Audit logging**: Enabled (tracks all deletions)

---

## 🆘 Troubleshooting

### Issue: Search box not filtering

**Solution:**

- Ensure you've loaded cases first (wait 2 seconds after login)
- Check if search box is active (click in it)
- Try clearing and retyping

### Issue: Edit doesn't work

**Solution:**

- Make sure you entered text in both prompts
- If first prompt is cancelled, it stops
- Check browser console for errors (F12)

### Issue: Delete shows error message

**Solution:**

- Confirm you have permission to delete
- Try refreshing the page and try again
- Check internet connection to server

### Issue: Transaction list is empty

**Solution:**

- No transactions added yet? Start by adding one
- Use "Add Transaction" form first
- Give it a moment to load after login

---

## 🔐 Security Notes

- ✅ All changes tracked in audit log
- ✅ Deletions require confirmation dialog
- ✅ User session required (login first)
- ✅ API validates all requests on server
- ✅ Database backups protect against data loss

---

## 📊 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Click search box | Focus for typing |
| Type | Filter in real-time |
| Escape | Exit prompts/dialogs |
| Tab | Move between fields |
| Enter | Confirm dialogs |

---

## 🎨 UI Elements Reference

| Icon | Meaning | Action |
|------|---------|--------|
| 🔍 | Search | Click input to search |
| ✏️ | Edit | Click to modify |
| 🗑️ | Delete | Click to remove |
| ✅ | Success | Action completed |
| ❌ | Error | Action failed |
| ⚠️ | Warning | Confirmation needed |

---

## 📝 FAQ

**Q: Can I undo a deletion?**
A: No. Deletions are permanent. Always confirm before deleting.

**Q: What gets deleted with a case?**
A: Only the case. Related transactions and assessments remain in database.

**Q: Can I edit other fields?**
A: Currently only title and description. More fields coming soon.

**Q: How long does search take?**
A: Instant - results appear as you type.

**Q: Is there a limit on search results?**
A: No - displays all matching results.

**Q: Can I delete multiple at once?**
A: Not yet - delete one at a time for now.

---

## 🚀 Next Steps

1. **Try searching** - Open any section and practice filtering
2. **Test edit** - Edit a case title to see how it works
3. **Try delete** - Delete a test case to understand confirmation
4. **Combine features** - Search, then edit/delete results

---

## 📞 Need Help?

If you encounter any issues:

1. Check the [Technical Documentation](TECHNICAL_DOCUMENTATION_EDIT_DELETE_SEARCH.md)
2. Review the [Features Guide](EDIT_DELETE_SEARCH_FEATURES.md)
3. Try refreshing your browser
4. Restart the server if needed

---

**You're all set! Enjoy the new features!** 🎉
