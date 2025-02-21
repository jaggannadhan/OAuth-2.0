# OAuth-2.0
This project demonstrates how OAuth works with various providers: Google, Facebook, GitHub, and Salesforce.

## What is OAuth?
OAuth is an open standard for access delegation, commonly used to grant websites or applications access to user information without exposing passwords.

## How it Works?
1. The user clicks the "Login with [Provider]" button on the frontend.
2. The backend redirects the user to [Providers]'s OAuth consent screen.
3. After granting permission, the [Provider] redirects the user back to the application with an authorization code.
4. The backend exchanges the authorization code for an access token and retrieves the user's profile information.

## End-to-End Flow Diagram
![googleOAuth2_0](https://github.com/user-attachments/assets/4aa05729-5ecb-49f7-84a4-0a0838ad6e51)

How to get the OAuth `client_id` and `client_secret`?

### Getting Google OAuth Client ID and Secret
1.  **Google Cloud Console:**
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create or select a project.

2.  **Credentials:**
    * Navigate to "APIs & Services" -> "Credentials".

3.  **Create Credentials:**
    * Click "Create Credentials" -> "OAuth client ID".

4.  **Application Type:**
    * Select the appropriate application type (e.g., Web application, Desktop app).
    * Configure authorized redirect URIs (for web apps).

5.  **Client ID and Secret:**
    * The Client ID and Client Secret will be displayed.
    * Download the JSON file for later use.
