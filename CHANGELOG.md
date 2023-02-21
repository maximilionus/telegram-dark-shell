# Dark Shell - Changelog


## Development

### iOS
#### Tweaked
- Links color tweaked to `#659dbe` and `#4f7a94`


## Update 2023.02.21 "Neue Welle"

> **Summary**
> This release contains various patches for the previous update

### Android 4.2
#### Fixed
- Chat list: Online status icon fixed again

### TDesktop 2.4
#### Fixed
- Chat background image color tweaked to match the overall scheme


## Update 2023.02.19 "Welle"

> **Summary**
> This small update is aimed at fixing existing issues and making minor improvements towards readability

### Android v4.1
#### Fixed
- Chat list
  - Mention icon color fix by [@kirzidev](https://github.com/kirizdev)
  - Online status icon color tweaked to white from green

### TDesktop v2.3
#### Fixed
- Tooltip background and border colors tweaked to dark
- Chat list: Saved messages icon gradient fixed to solid color
#### Tweaked
- Notification pop-up background color changed to lighter values to improve readability


## Update 2022.08.07 "Nachtstern"
Overhaul update for Android theme and some minor tweaks for Windows/Linux
### Android v4.0 - Release
#### Tweaked
- Chat submenu background color tweaked to light-gray value
- Profile page picture button background and icon colors inverted
- Archived chats top bar background color tweaked to darker values
- Saved messages icon background color tweaked to match color scheme
#### Fixed
- Tabs bar underline color corrected to match color scheme
- Chat input field cursor color now matches the color scheme
- Chat "admin" mark text color adjusted to match color scheme
- Tweaked colors of message "sent check" icons to more readable values
- Reply message field text color tweaked to more readable darker value
- Emoji panel selected tab underline color tweaked to match color scheme
- Floating button *(Like `send` in share menu)* colors now matches the color scheme
- Color of attachments in the dialogs list is now darker, almost equal to text color
- Chat pop-up panel *(Like `copy`, `save to gallery` and `copy link` actions)* background color tweaked to match color scheme

### TDesktop v2.2 - Release
#### Fixed
- Box background color linked to global background color
- Tooltip foreground color linked to global foreground color


## Update 2022.08.05
### TDesktop v2.1 - Release
#### Tweaked
- Media player bar background color adjusted to match title bar color
- Emoji bar background color tweaked to be more readable
#### Fixed
- Search/Filter input field background color now matches the color scheme


## Update 2022.08.02
### Android v3.0 Release
#### Fixed
- Selected text area background now displays properly
#### Tweaked
- Message input field now inherits the color from chat background (`#181818`)
- Text selection cursor color adjusted
#### Removed
- Pinned chats custom background removed

### TDesktop v2.0 Release
#### Tweaked
- Message input field now inherits the color from chat background (`#181818`)
- Search bars background now more consistent with theme color set

### iOS v2.0 Release
#### Tweaked
- Message input field now inherits the color from chat background (`#181818`)


## Update 2022.08.01
### Android v2.2 Release
#### Fixed
- Chat status bar color fixed

#### Tweaked
- In/Out chat messages text color modified to be more readable


## Update 2022.03.18
### TDesktop v1.2 Release
#### Fixed
- Title buttons color for inactive state now more consistent with title bar

### Global Changes
#### Changed
- Preview screenshot updated
  - Reflect current state
  - Fonts changed


## Update 2022.02.19
### Android v2.1 Release
#### Fixed
- Media buttons will now be displayed correctly, not just white circles
- Chat background image was updated and now will be displayed properly in cloud-synced theme

### Global Changes
#### Added
- Created `github workflow` for automated post-release actions

#### Changed
- Preview screenshot updated to current state


## Update 2022.01.07
### Android v2.0 Release
> In this update, significant changes have been made to the theme to match the current version of the client.  
> Here's my big sorries for cloud-synced theme users. There was some accident *22.01.07* with... uh well, theme.
#### Changed
- Remastered the structure of theme to make it more readable by current clients and services
- No more gray-colored gaps in menus. Theme will now look more consistent with `gray background` color attached to main `background` color
- Color for bottom navigation bar was adjusted to fit the theme looks

### TDesktop v1.1 Release
#### Fixed
- Icons color in context menus
#### Changed
- Color of the context menu separator

### Global Changes
#### Changed
- Preview screenshot updated to current state
- Enhanced the `VERSIONS_ARCHIVE.md` readability

#### Removed
- Details tag from `README.md` for preview image. Now image will load automatically.
