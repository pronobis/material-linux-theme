# material-linux - Auto-generated set of consistent themes for a Linux
#                  desktop based on the Android Material color palette.
#
# Copyright (C) 2014 Andrzej Pronobis
# Author: Andrzej Pronobis <a.pronobis@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

selected_palette = {
    # Background
    "bg-dark":            "#000000",
    "bg-normal":          "#121212",
    "bg-light":           "#212121",
    # Foreground
    "fg-light":           "#ffffff",
    "fg-normal":          "#dadada",
    "fg-dark":            "#969696",
    # Primary and accent colors
    "primary-light":      "indigo-300",
    "primary-normal":     "indigo-500",
    "primary-dark":       "indigo-700",
    "secondary-light":    "blue-grey-300",
    "secondary-normal":   "blue-grey-500",
    "secondary-dark":     "blue-grey-900",
    "accent-light":       "red-A100",
    "accent-normal":      "red-A400",
    "accent-dark":        "red-A700",
    "accent2-light":      "amber-A100",
    "accent2-normal":     "amber-A400",
    "accent2-dark":       "amber-A700",
    # Selected semantic colors
    "semantic1":          "teal-400",
    "semantic2":          "brown-400",
    "semantic3":          "lime-400",
    "semantic4":          "light-green-400",
    "semantic5":          "grey-600",
    "semantic6":          "grey-800",
    "semantic7":          "purple-300",  # 400 is simply too dark
    "semantic8":          "blue-400",
    "semantic9":          "green-400",
    "semantic10":         "pink-400",
    "semantic11":         "cyan-400",
    # Success/error/warning colors
    "error-light":        "red-200",
    "error-normal":       "red-400",
    "error-dark":         "#851414",
    "success-light":      "green-200",
    "success-normal":     "green-400",
    "success-dark":       "#144517",
    "warning-light":      "orange-200",
    "warning-normal":     "orange-400",
    "warning-dark":       "#994300",
    # Selected distinct colors
    "distinct1":          "lime-400",
    "distinct2":          "blue-400",
    "distinct3":          "pink-400",
    "distinct4":          "teal-400",
    "distinct5":          "brown-400",
    "distinct6":          "light-green-400",
    "distinct7":          "purple-400",
    "distinct8":          "cyan-400",
    "distinct9":          "green-400",
    # Selected colors by ansi names
    "black":              "#121212",
    "red":                "red-400",
    "green":              "green-400",
    "yellow":             "lime-400",
    "blue":               "blue-400",
    "magenta":            "pink-400",
    "cyan":               "cyan-400",
    "white":              "#dadada",
    "dark-black":         "#000000",
    "dark-red":           "red-600",
    "dark-green":         "green-600",
    "dark-yellow":        "lime-600",
    "dark-blue":          "blue-600",
    "dark-magenta":       "pink-600",
    "dark-cyan":          "cyan-600",
    "dark-white":         "#969696",
    "bright-black":       "#1f1f1f",
    "bright-red":         "red-200",
    "bright-green":       "green-200",
    "bright-yellow":      "lime-200",
    "bright-blue":        "blue-200",
    "bright-magenta":     "pink-200",
    "bright-cyan":        "cyan-200",
    "bright-white":       "#ffffff",
}


colors = {
    # Views
    "view-bg":                    "bg-normal",        # convenient for long use
    "view-tx":                    "fg-normal",
    "view-header-bg":             "secondary-dark",
    "view-header-tx":             "primary-light",
    "view-selected-bg":           "primary-dark",
    "view-selected-tx":           "fg-normal",    # keep standard text color if possible
    "view-selected-inactive-bg":  "secondary-dark",
    "view-selected-inactive-tx":  "fg-normal",
    "view-marked-bg":             "bg-normal",
    "view-marked-tx":             "accent2-normal",
    "view-marked-inactive-bg":    "bg-normal",
    "view-marked-inactive-tx":    "accent2-dark",
    "view-highlighted-bg":        "accent-normal",
    "view-highlighted-tx":        "bg-normal",
    "view-highlighted-inactive-bg": "accent2-normal",
    "view-highlighted-inactive-tx": "bg-normal",
    # Windows
    "window-bg":                  "bg-light",
    "window-tx":                  "fg-normal",
    "window-title-active-bg":     "primary-normal",
    "window-title-active-tx":     "fg-light",
    "window-title-inactive-bg":   "bg-light",
    "window-title-inactive-tx":   "fg-dark",
    "window-title-urgent-bg":     "accent-dark",
    "window-title-urgent-tx":     "fg-light",
    "window-button-active-bg":    "primary-dark",
    "window-button-active-tx":    "fg-light",
    "window-button-inactive-bg":  "bg-light",
    "window-button-inactive-tx":  "fg-dark",
    "window-button-urgent-bg":    "accent-normal",
    "window-button-urgent-tx":    "fg-light",
    # Panels
    "panel-bg":                   "bg-light",
    "panel-tx":                   "fg-normal",
    "panel-button-active-bg":     "primary-normal",
    "panel-button-active-tx":     "fg-light",
    "panel-button-inactive-bg":   "bg-light",
    "panel-button-inactive-tx":   "fg-dark",
    "panel-button-urgent-bg":     "accent-normal",
    "panel-button-urgent-tx":     "fg-light",
    # Menu
    "menu-bg":                    "secondary-dark",
    "menu-tx":                    "fg-normal",
    "menu-inactive-tx":           "fg-dark",
    "menu-selected-bg":           "primary-dark",
    "menu-selected-tx":           "fg-normal",
    # Tooltips
    "tooltip-bg":                 "fg-normal",
    "tooltip-tx":                 "bg-light",
    # Scrollbars
    "scrollbar-bg":               "bg-light",
    "scrollbar-fg":               "primary-dark",
    # Basic file types
    "file-broken-tx":             "accent-normal",
    "file-directory-tx":          "fg-light",
    "file-normal-tx":             "fg-normal",
    "file-link-tx":               "semantic4",
    "file-remote-tx":             "semantic4",  # Same as link
    "file-device-tx":             "semantic8",
    "file-special-tx":            "semantic2",
    "file-executable-tx":         "semantic3",
    "file-archive-tx":            "semantic7",
    "file-source-tx":             "semantic10",
    "file-document-tx":           "semantic1",
    "file-media-tx":              "semantic11",
    "file-temp-tx":               "semantic5",
    "file-readonly-tx":           "semantic9",
    "file-modified-tx":           "accent-normal",
    # Basic source code elements
    "source-string-tx":           "semantic1",
    "source-doc-tx":              "semantic2",
    "source-function-tx":         "semantic3",
    "source-variable-tx":         "semantic4",
    "source-comment-tx":          "semantic5",
    "source-comment-delim-tx":    "semantic6",
    "source-builtin-tx":          "semantic11",
    "source-keyword-tx":          "semantic8",
    "source-preprocessor-tx":     "semantic7",
    "source-type-tx":             "semantic10",
    "source-constant-tx":         "semantic9",
    "source-warning-tx":          "accent2-normal",  # DEPRECATED, USE WARNING
    "source-whitespace-bg":       "bg-light",
    "source-whitespace-tx":       "semantic5",
    # Text
    "text-link-tx":               "semantic8",
    "text-tag-tx":                "semantic11",
    "text-section1-tx":           "distinct1",
    "text-section2-tx":           "distinct2",
    "text-section3-tx":           "distinct3",
    "text-section4-tx":           "distinct4",
    "text-section5-tx":           "distinct5",
    # Basic VC elements
    "vc-branch-tx":               "semantic1",
    "vc-tag-tx":                  "semantic4",
    "vc-sha-tx":                  "semantic10",
    # Cursor
    "cursor-normal-bg":           "accent2-normal",
    "cursor-read-only-bg":        "semantic9",
    "cursor-overwrite-bg":        "accent-normal",
    "cursor-special-bg":          "semantic8",
    # Notification types
    "error-tx":                   "error-normal",
    "warning-tx":                 "warning-normal",
    "success-tx":                 "success-normal",
    # Diff
    "diff-add-tx":                "success-light",
    "diff-add-bg":                "success-dark",
    "diff-delete-tx":             "error-light",
    "diff-delete-bg":             "error-dark",
    "diff-change-tx":             "warning-light",
    "diff-change-bg":             "warning-dark",
    "diff-context-tx":            "fg-dark",
    "diff-context-bg":            "bg-normal"
}
