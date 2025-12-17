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
