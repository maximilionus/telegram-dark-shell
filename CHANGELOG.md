# Dark Shell - Changelog


## Development "Nebelschleier"

> **Summary**  
> Huge improvements for Desktop and Android themes by
> [@elifian](https://github.com/elifian)
> ([#21](https://github.com/maximilionus/telegram-dark-shell/pull/21))

### Android 4.5
#### Tweaked
- Background color of Saved Messages now matches the general background.
- Background of Music search bar in media attachments made more consistent.

#### Fixed
- Stickers & GIF search bar background color is dark now.
- Custom profile colors are now displayed correctly.
- Media player background color fixed.
- Send video button background is white now.
- Profile emoji status (including the verified badge) is now matching the
  overall white color.

### Desktop 2.5
#### Tweaked
- Title bar background is now more consistent with overall color scheme,
  matching the general background.

#### Fixed
- Custom profile colors are now displayed correctly.
- Profile emoji status (including the verified badge) is now matching the
  overall white color.


## Update 2023.04.26 "Dammerung-2"

> **Summary**  
> Small fix for Android theme *(by [@kirizdev](https://github.com/kirizdev))*

### Android 4.4
#### Fixed
- Bot menu icon color fix by [@kirizdev](https://github.com/kirizdev) (#15)


## Update 2023.03.16 "Dammerung"

> **Summary**  
> Major update for **iOS** platform and various fixes for **Android** *(by [@kirizdev](https://github.com/kirizdev))*

### iOS 3.0
#### Fixed
- GIF, Stickers and Emoji chat panel background and placeholder colors now match the color scheme
- Pinned chat background (inactive and selected) now match the color scheme
- Reactions foreground and background colors now match the color scheme
#### Tweaked
- Links color tweaked to `#659dbe` and `#4f7a94`

### Android 4.3
#### Fixed
- Forwarded message hidden user dialog background and text colors fix by [@kirizdev](https://github.com/kirizdev) (#12)
- Active radio button icon color fix by [@kirizdev](https://github.com/kirizdev) (#13)
- Emoji suggestion pop-up background color fix by [@kirizdev](https://github.com/kirizdev) (#13)
- "Add {name} to contacts" button text color fix by [@kirizdev](https://github.com/kirizdev) (#13)


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
  - Mention icon color fix by [@kirizdev](https://github.com/kirizdev) (#11)
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
