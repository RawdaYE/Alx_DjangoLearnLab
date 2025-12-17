# Bookshelf App Permissions and Groups

## Custom Permissions
Defined in `Book` model:
- `can_view` — allows viewing book instances
- `can_create` — allows creating books
- `can_edit` — allows editing books
- `can_delete` — allows deleting books

## Groups
- **Viewers** — assigned `can_view`
- **Editors** — assigned `can_view`, `can_create`, `can_edit`
- **Admins** — assigned all permissions

## Views
- `book_list` — protected by `can_view`
- `add_book` — protected by `can_create`
- `edit_book` — protected by `can_edit`
- `delete_book` — protected by `can_delete`

## Testing
- Created 3 users and assigned to groups
- Logged in as each user and visited the corresponding views
- Verified permissions:
  - Users without permission get **403 Forbidden**
  - Users with permission can access the page

## Notes
- CustomUser model used with `date_of_birth` and `profile_photo`
- Admin setup uses `UserAdmin` to allow group assignment


## Step 4: Deployment Configuration for HTTPS

In a production environment, HTTPS must be handled at the web server level
(e.g., Nginx or Apache) using SSL/TLS certificates.

Typical steps include:
- Installing an SSL certificate (e.g., via Let's Encrypt)
- Configuring the web server to listen on port 443
- Redirecting all HTTP traffic (port 80) to HTTPS
- Forwarding secure requests to Django using WSGI
- Setting the `X-Forwarded-Proto` header so Django knows the request is secure

This project assumes HTTPS is correctly configured at the deployment level,
and Django security settings (SECURE_SSL_REDIRECT, HSTS, secure cookies)
are used to enforce HTTPS usage.


## Step 5: Documentation and Security Review

### Implemented Security Measures

- HTTPS enforcement is enabled using `SECURE_SSL_REDIRECT` to ensure all
  HTTP requests are redirected to HTTPS.
- HTTP Strict Transport Security (HSTS) is configured using
  `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, and
  `SECURE_HSTS_PRELOAD` to force browsers to use HTTPS for all future requests.
- Secure cookies are enforced using `SESSION_COOKIE_SECURE` and
  `CSRF_COOKIE_SECURE`, ensuring sensitive cookies are only transmitted
  over encrypted connections.
- Clickjacking protection is implemented using `X_FRAME_OPTIONS = 'DENY'`.
- MIME-type sniffing is prevented using `SECURE_CONTENT_TYPE_NOSNIFF`.
- Basic XSS protection is enabled using `SECURE_BROWSER_XSS_FILTER`.

### Security Benefits

These settings ensure:
- Encrypted communication between clients and the server
- Protection against man-in-the-middle attacks
- Reduced risk of cross-site scripting (XSS) and clickjacking attacks
- Secure handling of authentication and session data

### Potential Improvements

- Use automated SSL certificate renewal (e.g., Let's Encrypt) in production
- Implement Content Security Policy (CSP) for stronger XSS protection
- Regular security audits and dependency updates

