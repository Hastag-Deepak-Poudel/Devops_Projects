# Google Sheets Integration Setup Guide

Follow these steps to connect your RSVP form to Google Sheets:

## Step 1: Create a Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it "RSVP Responses" (or whatever you prefer)
4. In the first row, add these column headers:
   - A1: First Name
   - B1: Last Name
   - C1: Email
   - D1: Phone
   - E1: Attending
   - F1: Guests
   - G1: Dietary Restrictions
   - H1: Submitted At

## Step 2: Create Google Apps Script

1. In your Google Sheet, click **Extensions** > **Apps Script**
2. Delete any code in the script editor
3. Copy and paste the following code:

```javascript
function doPost(e) {
  try {
    // Get the active spreadsheet
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Parse the incoming data
    var data = JSON.parse(e.postData.contents);
    
    // Create array of values to append
    var rowData = [
      data.firstName || '',
      data.lastName || '',
      data.email || '',
      data.phone || '',
      data.attending || '',
      data.guests || '',
      data.dietary || '',
      data.submittedAt || new Date().toLocaleString()
    ];
    
    // Append the row to the sheet
    sheet.appendRow(rowData);
    
    // Return success response
    return ContentService
      .createTextOutput(JSON.stringify({ 'result': 'success', 'row': sheet.getLastRow() }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    // Return error response
    return ContentService
      .createTextOutput(JSON.stringify({ 'result': 'error', 'error': error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

4. Click the **Save** icon (💾) or press Ctrl+S / Cmd+S
5. Name your project (e.g., "RSVP Form Handler")

## Step 3: Deploy the Script

1. Click **Deploy** > **New deployment**
2. Click the gear icon ⚙️ next to "Select type"
3. Choose **Web app**
4. Configure the deployment:
   - **Description**: RSVP Form Handler (or any description)
   - **Execute as**: Me (your email)
   - **Who has access**: Anyone
5. Click **Deploy**
6. You may need to authorize the script:
   - Click **Authorize access**
   - Choose your Google account
   - Click **Advanced** > **Go to [project name] (unsafe)**
   - Click **Allow**
7. **Copy the Web app URL** - it will look like:
   `https://script.google.com/macros/s/ABC123.../exec`

## Step 4: Update Your HTML File

1. Open your `professional-invitation-portal.html` file
2. Find this line (around line 1060):
   ```javascript
   const scriptURL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
   ```
3. Replace `'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE'` with your actual URL:
   ```javascript
   const scriptURL = 'https://script.google.com/macros/s/ABC123.../exec';
   ```
4. Save the file

## Step 5: Test It!

1. Open your HTML file in a browser
2. Fill out and submit the form
3. Check your Google Sheet - you should see a new row with the form data!

## Troubleshooting

**Form not submitting:**
- Check browser console for errors (F12 > Console tab)
- Make sure the script URL is correct
- Verify the script is deployed with "Anyone" access

**Data not appearing in sheet:**
- Check that column headers match exactly
- Look at the Apps Script logs: Apps Script > Executions

**Authorization issues:**
- Re-deploy the script
- Make sure you clicked "Allow" during authorization
- Try using an incognito/private browser window

## Important Notes

- The form data is sent to YOUR Google Sheet (not visible to form users)
- You can view, download, or analyze responses in the Google Sheet
- You can set up email notifications in Google Sheets: Tools > Notification rules
- The script runs under your Google account permissions

## Optional: Add Email Notifications

To get notified when someone submits:

1. In Google Sheets, click **Tools** > **Notification rules**
2. Choose "A user submits a form" or "Any changes are made"
3. Set notification frequency
4. Click **Save**

---

That's it! Your RSVP form is now connected to Google Sheets.
